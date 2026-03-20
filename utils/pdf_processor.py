import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.faiss import FAISS
from langchain_ollama.embeddings import OllamaEmbeddings

def process_pdf(file_path):
    """
    Load PDF, split text, create vectorstore using Ollama embeddings.
    Returns FAISS vectorstore object.
    """
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    docs = text_splitter.split_documents(documents)

    embeddings = OllamaEmbeddings(model=os.getenv("OLLAMA_EMBEDDING_MODEL"))
    vectorstore = FAISS.from_documents(docs, embeddings)

    return vectorstore