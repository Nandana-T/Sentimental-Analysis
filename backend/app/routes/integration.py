from fastapi import APIRouter
from app.services.integration_service import analyze_feedback

router = APIRouter(prefix="/analyze", tags=["Feedback Analysis"])

@router.post("/")
def analyze(feedback: dict):
    """
    API endpoint to analyze customer feedback.
    
    Args:
        feedback (dict): JSON request with "text" field.

    Returns:
        dict: Analysis result including emotion, topics, and Adorescore.
    """
    text = feedback.get("text", "")
    return analyze_feedback(text)
