import os
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from dotenv import load_dotenv
from utils.pdf_processor import process_pdf
from langchain_ollama.chat_models import ChatOllama
from langchain_classic.chains.retrieval_qa.base import RetrievalQA

# Load environment variables
load_dotenv()

app = FastAPI(title="PDF Chatbot API (RAG)")

# In-memory storage for vectorstore (per session)
vectorstore_storage = {}

@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF and process it to create a vectorstore for retrieval.
    """
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as f:
        f.write(await file.read())

    vectorstore = process_pdf(temp_file_path)
    vectorstore_storage["current"] = vectorstore

    return {"status": "success", "message": f"{file.filename} processed successfully!"}

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    """
    Ask a question based on the uploaded PDF.
    """
    if "current" not in vectorstore_storage:
        return {"status": "error", "message": "No PDF uploaded yet."}

    vectorstore = vectorstore_storage["current"]
    llm = ChatOllama(
        model=os.getenv("OLLAMA_CHAT_MODEL"),
        temperature=0.5
    )
    retriever = vectorstore.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )
    response = qa_chain.invoke(request.question)
    return {"status": "success", "answer": response}