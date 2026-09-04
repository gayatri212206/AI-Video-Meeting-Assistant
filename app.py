import os
import tempfile
import streamlit as st
from dotenv import load_dotenv

# Your custom imports
from utils.audio_processor import process_input
from core.transcriber import transcribe_all
from core.summarizer import summarize, generate_title
from core.extractor import (
    extract_action_items,
    extract_key_decisions,
    extract_questions,
)
from core.rag_engine import build_rag_chain, ask_question

load_dotenv()

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Meeting & Video Assistant",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom CSS for clean styling ---
st.markdown(
    """
    <style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1rem;
        color: #64748B;
        margin-bottom: 2rem;
    }
    .stMetric {
        background-color: #F8FAFC;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- Session State Initialization ---
if "pipeline_result" not in st.session_state:
    st.session_state.pipeline_result = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def run_pipeline_with_ui(source: str, language: str):
    """Executes pipeline steps with live progress feedback in UI."""
    with st.status("🚀 Processing Audio / Video...", expanded=True) as status:
        st.write("📥 Loading & processing input audio...")
        chunks = process_input(source)

        st.write(f"🗣️ Transcribing audio (Language: {language})...")
        transcript = transcribe_all(chunks, language)

        st.write("✨ Generating title & executive summary...")
        title = generate_title(transcript)
        summary = summarize(transcript)

        st.write("🔍 Extracting action items, decisions & questions...")
        action_items = extract_action_items(transcript)
        decisions = extract_key_decisions(transcript)
        questions = extract_questions(transcript)

        st.write("🧠 Building RAG Knowledge Base...")
        rag_chain = build_rag_chain(transcript)

        status.update(
            label="✅ Processing Complete!", state="complete", expanded=False
        )

    return {
        "title": title,
        "transcript": transcript,
        "summary": summary,
        "action_items": action_items,
        "key_decisions": decisions,
        "open_questions": questions,
        "rag_chain": rag_chain,
    }


# ==========================================
# SIDEBAR: Input & Controls
# ==========================================
with st.sidebar:
    st.title("⚙️ Configuration")

    input_mode = st.radio(
        "Select Source Type:",
        ["YouTube URL / Web Link", "Upload Local File"],
        index=0,
    )

    source_path = None

    if input_mode == "YouTube URL / Web Link":
        url_input = st.text_input(
            "Paste URL:",
            placeholder="https://www.youtube.com/watch?v=...",
        )
        if url_input.strip():
            source_path = url_input.strip()
    else:
        uploaded_file = st.file_uploader(
            "Choose an audio/video file",
            type=["mp3", "mp4", "wav", "m4a", "mov", "mkv"],
        )
        if uploaded_file is not None:
            # Save uploaded file to a temporary location
            temp_dir = tempfile.gettempdir()
            temp_path = os.path.join(temp_dir, uploaded_file.name)
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            source_path = temp_path

    language = st.selectbox(
        "Audio Language:",
        options=["english", "hinglish", "hindi", "spanish", "french", "auto"],
        index=0,
    )

    process_btn = st.button(
        "🚀 Process Video / Audio",
        type="primary",
        use_container_width=True,
    )

    if process_btn:
        if not source_path:
            st.warning("⚠️ Please provide a URL or upload a file first!")
        else:
            # Reset chat history for new file
            st.session_state.chat_history = []
            st.session_state.pipeline_result = run_pipeline_with_ui(
                source_path, language
            )
            st.rerun()

    st.markdown("---")
    if st.session_state.pipeline_result:
        if st.button("🗑️ Reset / Clear All", use_container_width=True):
            st.session_state.pipeline_result = None
            st.session_state.chat_history = []
            st.rerun()


# ==========================================
# MAIN PANEL: Results & Chatbot
# ==========================================
st.markdown('<div class="main-header">🎙️ AI Video & Meeting Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Summarize, extract insights, and chat with any audio or video.</div>', unsafe_allow_html=True)

if not st.session_state.pipeline_result:
    st.info("👈 Enter a YouTube URL or upload a media file in the sidebar and click **Process Video / Audio** to get started.")
else:
    result = st.session_state.pipeline_result

    # Display Meeting Title Header
    st.subheader(f"📌 {result['title']}")
    st.divider()

    # Tabs for Organized Insights
    tab_summary, tab_actions, tab_decisions, tab_transcript = st.tabs(
        ["📋 Summary", "✅ Action Items", "🔑 Key Decisions & Questions", "📝 Full Transcript"]
    )

    with tab_summary:
        st.markdown("### Executive Summary")
        st.markdown(result["summary"])
        st.download_button(
            label="📥 Download Summary",
            data=result["summary"],
            file_name="summary.txt",
            mime="text/plain",
        )

    with tab_actions:
        st.markdown("### ✅ Action Items")
        st.markdown(result["action_items"])

    with tab_decisions:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔑 Key Decisions")
            st.markdown(result["key_decisions"])
        with col2:
            st.markdown("### ❓ Open Questions")
            st.markdown(result["open_questions"])

    with tab_transcript:
        st.markdown("### 📝 Full Transcription")
        with st.expander("Click to view full transcript text", expanded=False):
            st.write(result["transcript"])
        st.download_button(
            label="📥 Download Full Transcript",
            data=result["transcript"],
            file_name="transcript.txt",
            mime="text/plain",
        )

    st.divider()

    # ==========================================
    # Phase 2: Interactive RAG Chatbot
    # ==========================================
    st.subheader("💬 Chat with this Meeting / Video")
    st.caption("Ask specific questions, clarify topics, or search for timestamps.")

    # Display past conversation history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User Question Input
    if user_prompt := st.chat_input("Ask a question about the video content..."):
        # 1. Append and render user message
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.markdown(user_prompt)

        # 2. Get answer from RAG Chain
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    answer = ask_question(result["rag_chain"], user_prompt)
                    st.markdown(answer)
                    st.session_state.chat_history.append({"role": "assistant", "content": answer})
                except Exception as e:
                    error_msg = f"❌ Error querying RAG chain: {e}"
                    st.error(error_msg)
                    st.session_state.chat_history.append({"role": "assistant", "content": error_msg})