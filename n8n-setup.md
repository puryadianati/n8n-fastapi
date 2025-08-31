# n8n + FastAPI Integration Setup

## Quick Start

1. Build and start the services:
```bash
docker-compose up --build
```

2. Access the services:
- n8n: http://localhost:5678 (admin/password)
- FastAPI: http://localhost:8000
- FastAPI docs: http://localhost:8000/docs

## n8n Workflow Configuration

### HTTP Request Node Setup
To call your FastAPI endpoints from n8n:

1. Add an HTTP Request node
2. Configure:
   - **Method**: POST/GET
   - **URL**: `http://fastapi:8000/webhook/process` (for webhook)
   - **URL**: `http://fastapi:8000/api/users` (for user creation)
   - **Headers**: `Content-Type: application/json`

### Troubleshooting Connection Issues

If you get "service refused connection":

1. **Check container status**: Run `docker-compose ps`
2. **Test from n8n container**: 
   ```bash
   docker exec purya-pc-n8n-1 wget -q --spider http://fastapi:8000/health
   ```
3. **Common fixes**:
   - Use `http://fastapi:8000` (not localhost)
   - Ensure both containers are on same network
   - Check FastAPI is listening on 0.0.0.0:8000

### Example HTTP Request Node Config:
- **Method**: GET
- **URL**: `http://fastapi:8000/health`
- **Authentication**: None
- **Body**: None (for GET requests)

### Available FastAPI Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `POST /webhook/process` - Process webhook data
- `POST /api/users` - Create user
- `GET /api/users/{user_id}` - Get user by ID

### Sample n8n Workflow

1. **Trigger**: Manual Trigger or Webhook
2. **HTTP Request**: Call FastAPI endpoint
3. **Set**: Process the response
4. **Output**: Use the processed data

## Environment Variables

FastAPI service uses `fastapi` as hostname within Docker network.
n8n can reach FastAPI at: `http://fastapi:8000`