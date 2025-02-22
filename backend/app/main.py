from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import emotions, topics, scoring

app = FastAPI(title="Customer Emotion Analysis System")

# Include API routes
app.include_router(emotions.router)
app.include_router(topics.router)
app.include_router(scoring.router)

@app.get("/")
def root():
    return {"message": "Customer Emotion Analysis API is running!"}

# Run using: uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
