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