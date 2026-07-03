# 🚀 Resume Copilot

An AI-powered Resume Assistant built using Python, ChromaDB, Sentence Transformers, and Google Gemini.

## ✨ Features

- 📄 Extract text from PDF resumes
- 🧠 Semantic search using ChromaDB
- 🤖 Chat with your resume using Google's Gemini
- 📂 Section-aware parsing (Education, Experience, Projects, Skills, Achievements)
- 🔍 Retrieval-Augmented Generation (RAG)

## 🛠️ Tech Stack

- Python 3.14
- Google Gemini API
- ChromaDB
- Sentence Transformers
- PyMuPDF
- LangChain (Text Splitting)

## 📁 Project Structure

```
Resume-Copilot
│
├── backend
│   ├── chatbot.py
│   ├── embeddings.py
│   ├── main.py
│   ├── parser.py
│   ├── rag.py
│   ├── vectorstore.py
│
├── data
├── requirements.txt
└── README.md
```

## 🚀 Installation

```bash
git clone https://github.com/YOUR_USERNAME/Resume-Copilot.git

cd Resume-Copilot

python -m venv .venv

.\.venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file:

```text
GOOGLE_API_KEY=YOUR_API_KEY
```

Run:

```bash
python backend/main.py
```

Then:

```bash
python backend/chatbot.py
```

## 📌 Future Improvements

- ATS Resume Score
- Resume vs Job Description Matching
- Cover Letter Generator
- Interview Question Generator
- Skill Gap Analysis
- FastAPI Backend
- React Frontend

## 📄 License

MIT License