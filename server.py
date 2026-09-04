import os
import uuid
import shutil
from typing import Optional
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# Pipeline Imports
from dotenv import load_dotenv
from utils.audio_processor import process_input
from core.transcriber import transcribe_all
from core.summarizer import summarize, generate_title
from core.extractor import extract_action_items, extract_key_decisions, extract_questions
from core.rag_engine import build_rag_chain, ask_question

load_dotenv()

app = FastAPI(title="AI Video Assistant")
templates = Jinja2Templates(directory="templates")

# Store active RAG chains in memory {session_id: rag_chain}
rag_sessions = {}

class ChatRequest(BaseModel):
    session_id: str
    question: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/process")
async def process_video(
    youtube_url: Optional[str] = Form(None),
    language: str = Form("english"),
    file: Optional[UploadFile] = File(None)
):
    source = None
    temp_path = None

    if youtube_url and youtube_url.strip():
        source = youtube_url.strip()
    elif file and file.filename:
        os.makedirs("temp_uploads", exist_ok=True)
        temp_path = os.path.join("temp_uploads", f"{uuid.uuid4()}_{file.filename}")
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        source = temp_path
    else:
        raise HTTPException(status_code=400, detail="Please provide a YouTube URL or upload a file.")

    try:
        # Run your pipeline
        chunks = process_input(source)
        transcript = transcribe_all(chunks, language)
        title = generate_title(transcript)
        summary = summarize(transcript)
        action_items = extract_action_items(transcript)
        decisions = extract_key_decisions(transcript)
        questions = extract_questions(transcript)
        rag_chain = build_rag_chain(transcript)

        # Save RAG session
        session_id = str(uuid.uuid4())
        rag_sessions[session_id] = rag_chain

        return JSONResponse({
            "session_id": session_id,
            "title": title,
            "summary": summary,
            "action_items": action_items,
            "key_decisions": decisions,
            "open_questions": questions,
            "transcript": transcript
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Cleanup uploaded temp file
        if temp_path and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except Exception:
                pass

@app.post("/api/chat")
async def chat_with_meeting(payload: ChatRequest):
    if payload.session_id not in rag_sessions:
        raise HTTPException(status_code=404, detail="Session expired. Please re-process your video.")
    
    rag_chain = rag_sessions[payload.session_id]
    answer = ask_question(rag_chain, payload.question)
    return {"answer": answer}