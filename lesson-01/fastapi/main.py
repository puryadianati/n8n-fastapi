
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

@app.post("/api/execute")
async def execute_task(data):
    # حالت 1: داده مستقیم از Google Sheets (آرایه)
    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict) and "price" in data[0]:
        prices = [item["price"] for item in data]
        names = [item["name"] for item in data]
        
        result = {
            "departments": names,
            "prices": prices,
            "total_price": sum(prices),
            "average_price": round(sum(prices) / len(prices), 2),
            "highest": {"name": names[prices.index(max(prices))], "price": max(prices)},
            "lowest": {"name": names[prices.index(min(prices))], "price": min(prices)},
            "department_count": len(data)
        }
        
        return {
            "status": "success",
            "message": "Google Sheets data processed",
            "data_source": "Excel/Google Sheets",
            "analysis": result
        }
    
    # حالت 2: فرمت method/params (از edit file یا manual)
    elif isinstance(data, dict) and "method" in data:
        method = data.get("method")
        params = data.get("params", {})
        
        if method == "create_from_list":
            numbers = params.get("data", [])
            result = {
                "sum": sum(numbers),
                "average": round(sum(numbers) / len(numbers), 2) if numbers else 0,
                "max": max(numbers) if numbers else 0,
                "min": min(numbers) if numbers else 0,
                "count": len(numbers)
            }
            return {
                "status": "success",
                "method": method,
                "data_source": "Manual/File",
                "input_data": numbers,
                "result": result
            }
    
    # حالت 3: هر داده دیگری
    return {
        "status": "received",
        "message": "Data received successfully",
        "input_data": data,
        "data_type": str(type(data))
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)