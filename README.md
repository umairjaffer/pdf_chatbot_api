# PDF Chatbot API (RAG)

### Project Overview:

A fully deployable PDF Chatbot API using Python, FastAPI, LangChain, Ollama embeddings, and FAISS.
Clients can upload PDF files and ask questions based on the content using AI-powered retrieval.

### Features:
- Upload PDF files and process them into vector embeddings
- Ask questions about the PDF content via API
- FastAPI-based backend for easy integration
- In-memory vectorstore for quick retrieval
- Fully configurable via environment variables
- Optional deployment to cloud (Render, Railway, Heroku)

```Folder Structure:
pdf_chatbot_api/
├── main.py                 # FastAPI API
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables template
├── utils/
│   └── pdf_processor.py    # PDF processing, embeddings, vectorstore
└── README.md               # Project instructions 
```

## Setup & Run:
1. Clone repository
   git clone <your-repo-url>
   cd pdf_chatbot_api
2. Create virtual environment (recommended)
   python -m venv venv
   # Activate virtual environment:
   # Windows:
   venv\Scripts\activate
   # macOS / Linux:
   source venv/bin/activate
3. Install dependencies
   pip install -r requirements.txt
4. Configure environment variables
   # Copy .env.example to .env
   # Windows:
   copy .env.example .env
   # macOS / Linux:
   cp .env.example .env
   # Edit .env and add your API keys:
   # OLLAMA_API_KEY=your_ollama_api_key_here
   # OLLAMA_EMBEDDING_MODEL=nomic-embed-text:latest
   # OLLAMA_CHAT_MODEL=qwen3.5:0.8b
5. Run FastAPI server
   uvicorn main:app --reload --host 0.0.0.0 --port 8000

API Usage:
- Upload PDF: POST /upload_pdf
  Form-data: file=@your_pdf_file.pdf
  Example curl:
  curl -X POST "http://localhost:8000/upload_pdf" -F "file=@sample.pdf"
  Response:
  {"status": "success", "message": "sample.pdf processed successfully!"}

- Ask Question: POST /ask
  JSON Body: {"question": "Your question here"}
  Example curl:
  curl -X POST "http://localhost:8000/ask" -H "Content-Type: application/json" -d '{"question":"What is AI?"}'
  Response:
  {"status": "success", "answer": "Artificial Intelligence (AI) is the field of ..."}

Deployment Instructions (Optional):
1. Push repository to GitHub
2. Connect repository to Render / Railway / Heroku
3. Add .env variables in platform dashboard
4. Deploy → Client receives API URL
5. Client can call endpoints directly via curl/Postman

Notes / Recommendations:
- Vectorstore is in-memory; for large PDFs, implement persistent storage
- Include demo video showing PDF upload → ask question → AI response
- API can be integrated into websites, mobile apps, or workflow automation
- Optional enhancements: Slack / Email / n8n workflow integration

Technology Stack:
- Python 3.10+
- FastAPI → REST API
- LangChain + Ollama → RAG, embeddings, LLM
- FAISS → Vectorstore
- dotenv → Environment variable management
- Optional: Docker for production