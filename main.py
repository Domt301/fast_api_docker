from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="EKS FastAPI App")


class HealthResponse(BaseModel):
    status: str
    message: str


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI on EKS"}

@app.get("/weather")
async def get_weather():
    return {"location": "EKS", "temperature": "22°C", "condition": "Sunny"}

@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        message="Application is running"
    )


@app.get("/api/info")
async def info():
    return {
        "app": "FastAPI EKS Application",
        "version": "1.0.0",
        "environment": "production"
    }
