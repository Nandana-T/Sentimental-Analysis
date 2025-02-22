from fastapi import APIRouter
from app.services.emotion_service import predict_emotion

router = APIRouter(prefix="/emotions", tags=["Emotion Detection"])

@router.post("/predict")
def get_emotion(feedback: dict):
    text = feedback["text"]
    return predict_emotion(text)
