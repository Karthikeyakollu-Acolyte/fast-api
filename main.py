from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request model
class ProcessDocumentRequest(BaseModel):
    s3_bucket_name: str
    user_id: str
    doc_id: str

@app.post("/process-document")
def process_document(request: ProcessDocumentRequest):
    print(f"Processing document: {request.doc_id} from {request.s3_bucket_name} by user {request.user_id}")
    return {"message": "Document processed", "doc_id": request.doc_id}

@app.get("/generation")
def generation(s3_bucket_name: str, user_id: str, doc_id: str, user_query: str):
    print(f"Generating response for {doc_id} from {s3_bucket_name} by user {user_id} with query: {user_query}")
    return {"message": "Generated response", "query": user_query}

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
