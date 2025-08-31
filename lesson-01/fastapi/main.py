from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any
import uvicorn

app = FastAPI(title="n8n Integration API", version="1.0.0")

class WebhookData(BaseModel):
    data: Dict[str, Any]

class ProcessResult(BaseModel):
    success: bool
    message: str
    processed_data: Dict[str, Any]

@app.get("/")
async def root():
    return {"message": "FastAPI service for n8n integration"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "fastapi-n8n"}

@app.post("/webhook/process")
async def process_webhook(data: WebhookData):
    processed_data = {
        "original": data.data,
        "processed_at": "2024-01-01T00:00:00Z",
        "processed": True
    }
    
    return ProcessResult(
        success=True,
        message="Data processed successfully",
        processed_data=processed_data
    )

@app.post("/api/users")
async def create_user(user_data: Dict[str, Any]):
    return {
        "id": 123,
        "name": user_data.get("name", "Unknown"),
        "email": user_data.get("email", "unknown@example.com"),
        "created": True
    }

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    return {
        "id": user_id,
        "name": f"User {user_id}",
        "email": f"user{user_id}@example.com"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)