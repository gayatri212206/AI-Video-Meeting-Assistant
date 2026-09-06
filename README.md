# 🤖 AI Video Meeting Assistant

> AI-powered meeting assistant for transcription, summarization, action items, key decisions, and RAG-based meeting chat.

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-green)](https://www.langchain.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Database-purple)](https://www.trychroma.com/)
#  AI Video Meeting Assistant

> **An AI-powered web application that transforms audio/video meetings into intelligent, structured, searchable, and actionable meeting reports.**

The **AI Video Meeting Assistant** helps users save time by automatically transcribing meetings, generating summaries, extracting action items and key decisions, identifying open questions, and allowing users to **chat with their meeting content using Retrieval-Augmented Generation (RAG).**

It supports **English, Hindi, and Hinglish** meetings and can also process **YouTube video URLs**.

---

##  Features

###  Audio & Video Support

* Upload audio/video meeting files
* Process YouTube video URLs
* Extract audio automatically for transcription
* FFmpeg-based audio/video processing

###  AI-Powered Transcription

* **Whisper AI** for English transcription
* **Sarvam AI** for Hindi and Hinglish transcription
* Converts meeting speech into searchable text

###  Intelligent Meeting Summarization

Automatically generates:

*  Meeting title
*  Concise meeting summary
*  Important discussion points

###  Action Items Extraction

Automatically identifies:

* Tasks discussed during the meeting
* Assigned work
* Important follow-up actions

###  Key Decisions Extraction

Extracts the major decisions made during the meeting so users don't have to go through the complete transcript.

###  Open Questions

Identifies:

* Unanswered questions
* Pending discussion points
* Issues requiring further clarification

###  Chat With Your Meeting

Users can ask questions directly about their meeting.

For example:

> **What were the main decisions made?**

> **What tasks were assigned to the team?**

> **What questions are still unanswered?**

The system uses **RAG + ChromaDB** to retrieve relevant sections of the meeting transcript before generating an answer.

---

#  How It Works

```text
                    ┌─────────────────────────┐
                    │    Video / Audio      │
                    │      YouTube URL        │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    Audio Processing   │
                    │        FFmpeg            │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      Transcription    │
                    │                         │
                    │  Whisper / Sarvam AI    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    Meeting Analysis   │
                    │                         │
                    │  • Summary              │
                    │  • Action Items         │
                    │  • Key Decisions        │
                    │  • Open Questions       │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       RAG Pipeline    │
                    │                         │
                    │ LangChain + ChromaDB    │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      Meeting Chat    │
                    │                         │
                    │ Ask Questions & Get     │
                    │ Context-Aware Answers   │
                    └─────────────────────────┘
```

---

#  RAG Pipeline

One of the main features of this project is the **Retrieval-Augmented Generation (RAG)** based meeting chat.

Instead of sending the entire meeting transcript directly to the language model, the transcript is divided into smaller chunks and converted into vector embeddings.

These embeddings are stored in **ChromaDB**, allowing the system to retrieve the most relevant parts of the meeting when the user asks a question.

```text
Meeting Transcript
        │
        ▼
   Text Chunking
        │
        ▼
Hugging Face Embeddings
        │
        ▼
    ChromaDB
 Vector Database
        │
        ▼
  Similarity Search
        │
        ▼
 Relevant Context
        │
        ▼
    Mistral LLM
        │
        ▼
   AI-Generated Answer
```

### Why RAG?

RAG makes it possible to ask questions about long meeting transcripts without manually searching through the entire conversation.

For example:

```text
User:
"What did the team decide about the project deadline?"

             ↓

RAG retrieves the relevant transcript section

             ↓

Mistral LLM generates the answer

             ↓

Answer:
"The team decided to complete the project by..."
```

---

# 🛠️ Tech Stack

##  Programming

* Python

##  Frontend

* HTML5
* CSS3
* JavaScript

## 🤖 AI / ML

* OpenAI Whisper
* Sarvam AI
* Mistral AI
* Hugging Face Embeddings

## 🔍 RAG & Vector Database

* LangChain
* ChromaDB
* Retrieval-Augmented Generation (RAG)

## 🎵 Audio / Video Processing

* FFmpeg
* yt-dlp
* Pydub


---

#  Application Workflow

### Step 1 — Provide Meeting Input

Upload an audio/video file or provide a YouTube video URL.

### Step 2 — Audio Processing

The application processes the input and extracts the required audio using FFmpeg and related tools.

### Step 3 — Transcription

The system automatically converts speech into text using the appropriate transcription technology.

### Step 4 — Meeting Analysis

The AI analyzes the transcript and generates:

* Meeting Title
* Summary
* Action Items
* Key Decisions
* Open Questions

### Step 5 — Build RAG Knowledge Base

The transcript is chunked, embedded, and stored in ChromaDB.

### Step 6 — Ask Questions

Users can interact with the meeting through the chat interface and receive context-aware answers.

---

#  Installation

## 1. Clone the Repository

```bash
git clone https://github.com/gayatri212206/AI-Video-Meeting-Assistant.git
```

Move into the project directory:

```bash
cd AI-Video-Meeting-Assistant
```

---

## 2. Create a Virtual Environment

Creating a virtual environment is recommended.

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

If you are using PowerShell and encounter an execution-policy error:

```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```

Then activate the environment again:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

After activation, you should see:

```text
(venv)
```

at the beginning of your terminal prompt.

---

# 📦 Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

If `pip` is unavailable, use:

```bash
python -m pip install -r requirements.txt
```

---

# 🎵 Install FFmpeg

FFmpeg is required for processing audio and video files.

Verify the installation:

```bash
ffmpeg -version
```

If the FFmpeg version information appears in the terminal, FFmpeg is installed correctly.

### ⚠️ FFmpeg Not Found?

If you get:

```text
ffmpeg is not recognized as the name of a cmdlet
```

make sure FFmpeg is installed and its `bin` directory has been added to the system **PATH**.

---

# 🔑 Environment Variables

The project uses API keys for AI services.

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key
SARVAM_API_KEY=your_sarvam_api_key
```



# ▶️ Running the Project

Start the Python backend according to the project's backend entry file.

For example:

```bash
python server.py
```

or:

```bash
python main.py
```

Then open the frontend:

```text
index.html
```

in your browser.

> Use the backend command corresponding to the entry file in your current project.

---

# 💡 Example Questions

After processing a meeting, users can ask questions such as:

```text
What were the main decisions made in the meeting?
```

```text
What tasks were assigned to each team member?
```

```text
What is the project deadline?
```

```text
What problems were discussed?
```

```text
What questions remain unanswered?
```

```text
Summarize the discussion about the project.
```

---

# 🎯 Use Cases

The AI Video Meeting Assistant can be useful for:

*  Business meetings
*  Software development meetings
*  College project meetings
*  Lectures and educational sessions
*  Team discussions
*  Interviews
*  YouTube video analysis
*  Meeting documentation

---

# 🌟 Key Benefits

###  Saves Time

Users don't need to watch or read an entire meeting to understand what happened.

###  Automated Analysis

Important information is extracted automatically from the transcript.

###  Searchable Knowledge

RAG allows users to retrieve relevant information from the meeting.

###  Interactive

Instead of simply reading a summary, users can ask questions and interact with the meeting content.



---

# 🔮 Future Improvements

* [ ] Speaker identification / diarization
* [ ] Real-time meeting transcription
* [ ] Multi-language UI
* [ ] DOCX report export
* [ ] Automatic action-item tracking
* [ ] Calendar integration
* [ ] User authentication
* [ ] Meeting history and dashboard
* [ ] Fully local LLM support
* [ ] Improved real-time processing
* [ ] Speaker-wise meeting summaries

---

# 👩‍💻 Author

### Gayatri Mohite

**B.Sc. Computer Science Student**

🔗 **GitHub:**
https://github.com/gayatri212206


---

# 📜 License

This project is created for **educational and project-development purposes**.
