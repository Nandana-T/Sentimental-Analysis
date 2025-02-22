from fastapi import APIRouter
from app.services.scoring_service import calculate_adorescore

router = APIRouter(prefix="/scoring", tags=["Adorescore Calculation"])

@router.post("/calculate")
def get_adorescore(data: dict):
    emotion = data["emotion"]
    topics = data["topics"]
    return calculate_adorescore(emotion, topics)
