from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
from app.schemas import DocumentRequest
import chromadb
from uuid import uuid4

model = SentenceTransformer( "sentence-transformers/all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./vectordb")

collection = client.get_or_create_collection(name="docs")

app = FastAPI()

@app.post("/documents")
def add_document(request:DocumentRequest):

    embedding = model.encode(request.text).tolist()

    collection.add(
        ids=[str(uuid4())],
        documents=[request.text],
        embeddings=[embedding]
    )

    return {"message": "Document is stored as Embeddings"}


@app.get("/serach")
def search_documents(query:str):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    return results

