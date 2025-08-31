# n8n + FastAPI Integration Course

دوره یکپارچه‌سازی n8n با FastAPI برای اتوماسیون و API های پیشرفته

## ساختار دروس

### درس ۱: راه‌اندازی اولیه
- FastAPI پایه
- Docker setup  
- n8n integration
- **فولدر**: `lesson-01/`

### درس ۲: API های پیشرفته
- User management
- Task management
- Database simulation
- **فولدر**: `lesson-02/`

### درس ۳: پایگاه داده واقعی
- PostgreSQL integration
- SQLAlchemy ORM
- **فولدر**: `lesson-03/`

### درس ۴: Authentication & Security  
- JWT tokens
- User authentication
- **فولدر**: `lesson-04/`

### درس ۵: پروژه نهایی
- Complete application
- Production deployment
- **فولدر**: `lesson-05/`

## نحوه اجرا

هر درس در فولدر جداگانه:
```bash
cd lesson-01
docker-compose up --build
```

## Git Workflow

برای هر درس:
```bash
git add .
git commit -m "Lesson X: توضیحات تغییرات"
git push
```