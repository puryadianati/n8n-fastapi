from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List
import uvicorn
from datetime import datetime

app = FastAPI(title="n8n Integration API - Lesson 2", version="2.0.0")

# Database simulation
users_db = {}
tasks_db = {}

class User(BaseModel):
    name: str
    email: str
    age: int

class Task(BaseModel):
    title: str
    description: str
    completed: bool = False

class WebhookData(BaseModel):
    data: Dict[str, Any]

@app.get("/")
async def root():
    return {"message": "FastAPI Lesson 2 - Advanced endpoints with database"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "fastapi-lesson2", "users_count": len(users_db)}

@app.post("/webhook/process")
async def process_webhook(data: WebhookData):
    processed_data = {
        "original": data.data,
        "processed_at": datetime.now().isoformat(),
        "processed": True,
        "lesson": "02"
    }
    return processed_data

@app.post("/api/users")
async def create_user(user: User):
    user_id = len(users_db) + 1
    users_db[user_id] = {
        "id": user_id,
        "name": user.name,
        "email": user.email,
        "age": user.age,
        "created_at": datetime.now().isoformat()
    }
    return users_db[user_id]

@app.get("/api/users")
async def get_all_users():
    return {"users": list(users_db.values()), "total": len(users_db)}

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.post("/api/users/{user_id}/tasks")
async def create_task(user_id: int, task: Task):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    task_id = len(tasks_db) + 1
    tasks_db[task_id] = {
        "id": task_id,
        "user_id": user_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
        "created_at": datetime.now().isoformat()
    }
    return tasks_db[task_id]

@app.get("/api/users/{user_id}/tasks")
async def get_user_tasks(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_tasks = [task for task in tasks_db.values() if task["user_id"] == user_id]
    return {"tasks": user_tasks, "total": len(user_tasks)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)