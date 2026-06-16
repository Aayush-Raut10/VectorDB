from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import chromadb

app = FastAPI(title="Vector DB Learning API")

# 1. Connect to ChromaDB (saves data to a folder named 'vector_storage')
chroma_client = chromadb.PersistentClient(path="./vector_storage")
collection = chroma_client.get_or_create_collection(name="learning_collection")


# 2. Define data structures for FastAPI input validation
class DocumentInput(BaseModel):
    id: str
    text: str

class SearchQuery(BaseModel):
    query: str
    num_results: int = 1



# 3. Endpoint to save data into the Vector DB
@app.post("/add-document")
def add_document(item: DocumentInput):
    try:
        collection.add(
            documents=[item.text],
            ids=[item.id]
        )
        return {"status": "success", "message": f"Document {item.id} saved successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# 4. Endpoint to search the Vector DB
@app.post("/search")
def search_vector_db(search: SearchQuery):
    try:
        results = collection.query(
            query_texts=[search.query],
            n_results=search.num_results
        )
        
        # Format the response nicely for the user
        return {
            "query": search.query,
            "matched_documents": results["documents"][0],
            "matched_ids": results["ids"][0]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
