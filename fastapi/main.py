# FastAPI Smart Data Science Tool
# Lesson 1: Building Your First Intelligent Data Science Tool

# Import required libraries
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from typing import Dict, Any, List, Union
import uvicorn

# Create FastAPI application
app = FastAPI(title="Smart Data Science Tool", description="Intelligent API for data science operations with n8n integration")

# Define input command model
class Command(BaseModel):
    method: str
    params: Dict[str, Any] = {}

# Main endpoint for executing commands
@app.post("/api/execute")
def execute_command(command: Command):
    """
    Execute data science commands based on method and parameters
    
    Available methods:
    - create_from_list: Convert a list to NumPy array
    - zeros: Create array filled with zeros
    """
    
    # Extract method and parameters from command
    method = command.method
    params = command.params

    if method == "create_from_list":
        # Command 1: Convert list to NumPy array
        data = params.get("data")
        if data is None:
            return {"status": "error", "message": "Parameter 'data' is required."}
        
        if not isinstance(data, list):
            return {"status": "error", "message": "Parameter 'data' must be a list."}
        
        try:
            numpy_array = np.array(data)
            return {
                "status": "success", 
                "output": numpy_array.tolist(),
                "info": {
                    "original_data": data,
                    "array_shape": list(numpy_array.shape),
                    "array_dtype": str(numpy_array.dtype),
                    "total_elements": int(numpy_array.size)
                }
            }
        except Exception as e:
            return {"status": "error", "message": f"Error creating array: {str(e)}"}

    elif method == "zeros":
        # Command 2: Create array filled with zeros
        shape = params.get("shape")
        if shape is None:
            return {"status": "error", "message": "Parameter 'shape' is required."}

        try:
            numpy_array = np.zeros(shape, dtype=int)
            return {
                "status": "success",
                "output": numpy_array.tolist(),
                "info": {
                    "shape": list(numpy_array.shape) if hasattr(numpy_array.shape, '__iter__') else [numpy_array.shape],
                    "total_elements": int(numpy_array.size),
                    "array_dtype": str(numpy_array.dtype)
                }
            }
        except Exception as e:
            return {"status": "error", "message": f"Error creating zeros array: {str(e)}"}

    # Unknown command
    return {"status": "error", "message": f"Unknown command: '{method}'. Available methods: create_from_list, zeros"}

# Health check endpoint
@app.get("/")
def read_root():
    return {
        "message": "Smart Data Science Tool API is running!", 
        "status": "healthy",
        "version": "1.0.0",
        "description": "FastAPI service for intelligent data science operations with n8n integration"
    }

# Get available methods
@app.get("/api/methods")
def get_available_methods():
    """
    Get all available methods and their usage examples
    """
    return {
        "available_methods": [
            {
                "method": "create_from_list",
                "description": "Convert a list to NumPy array for data processing",
                "required_params": ["data"],
                "example": {
                    "method": "create_from_list",
                    "params": {"data": [120, 155, 132, 180, 201]}
                },
                "use_case": "Convert sales data, measurements, or any list of numbers into optimized NumPy arrays"
            },
            {
                "method": "zeros",
                "description": "Create array filled with zeros for templates and initialization",
                "required_params": ["shape"],
                "example": {
                    "method": "zeros",
                    "params": {"shape": 12}
                },
                "use_case": "Create empty templates for monthly reports, forecast placeholders, or data initialization"
            }
        ]
    }

# Legacy endpoint for n8n compatibility
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "smart-data-science-tool"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)