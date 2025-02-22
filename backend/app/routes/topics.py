from fastapi import APIRouter
from app.services.topic_service import predict_topics

router = APIRouter(prefix="/topics", tags=["Topic Analysis"])

@router.post("/predict")
def get_topics(feedback: dict):
    text = feedback["text"]
    return predict_topics(text)
