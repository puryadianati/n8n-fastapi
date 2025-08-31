@echo off
setlocal

if "%1"=="start" (
    echo Starting n8n and FastAPI services...
    docker-compose up -d
    echo Services started. Access:
    echo n8n: http://localhost:5678
    echo FastAPI: http://localhost:8000
) else if "%1"=="stop" (
    echo Stopping services...
    docker-compose down
    echo Services stopped. Data is preserved in volumes.
) else if "%1"=="restart" (
    echo Restarting services...
    docker-compose restart
    echo Services restarted.
) else if "%1"=="logs" (
    if "%2"=="" (
        docker-compose logs -f
    ) else (
        docker-compose logs -f %2
    )
) else if "%1"=="status" (
    docker-compose ps
) else if "%1"=="clean" (
    echo This will remove all data! Press Ctrl+C to cancel.
    pause
    docker-compose down -v
    echo All data removed.
) else (
    echo Usage: manage.bat [command]
    echo Commands:
    echo   start    - Start services
    echo   stop     - Stop services (keeps data)
    echo   restart  - Restart services
    echo   logs     - Show logs (optional: logs fastapi or logs n8n)
    echo   status   - Show service status
    echo   clean    - Remove all data and containers
)