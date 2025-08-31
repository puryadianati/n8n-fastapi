# main.py

# 1. وارد کردن کتابخانه‌های لازم
from fastapi import FastAPI
from pantic import BaseModel
import numpy as np
from typing import Dict, Any

# 2. ساخت اپلیکیشن FastAPI
app = FastAPI(title="ابزار هوشمند علم داده")

# 3. تعریف مدل یا الگوی دستور ورودی ما
class Command(BaseModel):
    method: str
    params: Dict[str, Any] = {}

# 4. ساخت تنها Endpoint پروژه ما!
@app.post("/api/execute")
def execute_command(command: Command):
    """ این تابع دستورات را دریافت و پردازش می‌کند """

    # 5. مغز متفکر: بخش تصمیم‌گیری بر اساس دستور
    method = command.method
    params = command.params

    if method == "create_from_list":
        # --- منطق مربوط به دستور اول ---
        data = params.get("data")
        if data is None:
            return {"status": "error", "message": "پارامتر 'data' یافت نشد."}
        
        numpy_array = np.array(data)
        return {
            "status": "success", 
            "output": numpy_array.tolist()
        }

    elif method == "zeros":
        # --- منطق مربوط به دستور دوم ---
        shape = params.get("shape")
        if shape is None:
            return {"status": "error", "message": "پارامتر 'shape' یافت نشد."}

        numpy_array = np.zeros(shape, dtype=int)
        return {
            "status": "success",
            "output": numpy_array.tolist()
        }

    # اگر دستوری بفرستیم که بلد نیست
    return {"status": "error", "message": f"دستور '{method}' ناشناخته است."}