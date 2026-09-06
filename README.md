🤖 AI Video Meeting Assistant

An AI-powered meeting assistant that converts audio/video meetings and YouTube videos into structured, searchable meeting reports.

The application can transcribe meetings, generate summaries, extract important information, and allow users to chat with their meeting content using RAG (Retrieval-Augmented Generation).

✨ Features
🎥 Video & Audio Support
Upload audio/video files
Process YouTube video URLs
📝 AI Transcription
Local Whisper AI for English meetings
Sarvam AI for Hindi & Hinglish transcription
🧠 AI Meeting Summarization
Automatically generates concise meeting summaries
Generates a suitable title for the meeting
✅ Action Items Extraction
Identifies tasks discussed during the meeting
Helps track what needs to be done
📌 Key Decisions Extraction
Extracts important decisions made during the meeting
❓ Open Questions
Identifies unanswered questions and discussion points
💬 Chat with Your Meeting
Ask questions about the meeting
Uses RAG + ChromaDB to retrieve relevant information before generating answers

How It Works
              ┌──────────────────────┐
              │   Video / Audio /    │
              │     YouTube URL      │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Audio Processing   │
              │      + FFmpeg        │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │     Transcription    │
              │ Whisper / Sarvam AI  │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Meeting Analysis   │
              │                      │
              │ • Summary            │
              │ • Action Items       │
              │ • Key Decisions      │
              │ • Questions          │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │     RAG Pipeline     │
              │ LangChain + ChromaDB │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Ask Questions &    │
              │   Chat with Meeting  │
              └──────────────────────┘

              Tech Stack

              AI / ML
OpenAI Whisper
Sarvam AI
Mistral AI
Hugging Face Embeddings
RAG
LangChain
ChromaDB
Retrieval-Augmented Generation (RAG)
Audio / Video Processing
FFmpeg
yt-dlp
Pydub

Installation
Step 1: Open Terminal and Navigate to the Project Folder
Open your terminal (or VS Code integrated terminal) and navigate to the directory where your server.py file is located:
code
Bash
cd path/to/your/project-folder
(If server.py is inside a backend folder, run cd backend).
Step 2: Create & Activate a Virtual Environment (Recommended)
If you haven't created a virtual environment yet, create one:
code
Bash
python -m venv venv
Now, activate it:
Windows (Command Prompt / PowerShell):
code
Bash
venv\Scripts\activate
(If you get a script execution policy error in PowerShell, run: Set-ExecutionPolicy Unrestricted -Scope Process first).
macOS / Linux:
code
Bash
source venv/bin/activate
(Once activated, you will see (venv) at the beginning of your terminal prompt).
Step 3: Install Required Dependencies
Install the necessary packages listed in your requirements.txt:
code
Bash
pip install -r requirements.txt
(If you don't have a requirements.txt file, install the standard packages manually, e.g.: pip install fastapi uvicorn openai python-dotenv or pip install flask flask-cors).
Step 4: Set Up the .env File (API Keys)
Create a .env file in the same directory as server.py and add your required keys and configuration:
code
Env
OPENAI_API_KEY=your_actual_api_key_here
PORT=8000
Step 5: Run server.py
Depending on how your server code is written, choose one of the following methods:
Method 1: Direct Python Execution (For Flask or standard scripts)
code
Bash
python server.py
Method 2: Using Uvicorn (For FastAPI applications)
code
Bash
uvicorn server:app --reload --port 8000
(Here, server refers to server.py, and app refers to the FastAPI application instance).
Step 6: Verify the Server is Running
You should see output in the terminal similar to:
code
Text
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
Test it in your browser:
Base URL: http://localhost:8000 (or http://localhost:5000)
API Documentation (FastAPI): http://localhost:8000/docs
⚠️ Common Errors & Fixes:
ModuleNotFoundError: No module named '...'
👉 Install the missing module directly: pip install <module_name>.
Address already in use / Port busy
👉 Change the port when running: uvicorn server:app --reload --port 8080 or terminate the process running on that port.
FFmpeg not found
👉 If your assistant processes audio/video files, make sure FFmpeg is installed on your operating system and added to your system's PATH.

Environment Variables

Create a .env file in the project root:

MISTRAL_API_KEY=your_mistral_api_key
SARVAM_API_KEY=your_sarvam_api_key

Usage
Step 1 — Provide Meeting Input

Upload an audio/video file or provide a YouTube URL.

Step 2 — Transcription

The system extracts the audio and converts the speech into text.

Step 3 — Meeting Analysis

The AI generates:

Meeting title
Summary
Action items
Key decisions
Open questions
Step 4 — Chat with Meeting

Ask questions such as:

What were the main decisions made?
What tasks were assigned to the team?
What questions remain unanswered?

The RAG pipeline retrieves relevant sections from the meeting transcript before generating the answer.

RAG Pipeline

The meeting transcript is divided into smaller chunks and converted into vector embeddings.

Meeting Transcript
        ↓
Text Chunking
        ↓
Hugging Face Embeddings
        ↓
ChromaDB Vector Store
        ↓
Similarity Search
        ↓
Relevant Context
        ↓
Mistral LLM
        ↓
AI Answer

This allows users to ask questions about long meetings without manually searching through the entire transcript.

Future Improvements

Speaker identification / diarization

Multi-language UI

DOCX export

Automatic meeting action-item tracking

Calendar integration

User authentication

Meeting history and dashboard

Fully local LLM option

Improved real-time meeting transcription


 Author

Gayatri Mohite

B.Sc. Computer Science Student
https://github.com/gayatri212206



 License

This project is created for educational and project-development purposes.
