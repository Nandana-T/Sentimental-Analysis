from app.services.emotion_service import predict_emotion
from app.services.topic_service import predict_topics
from app.services.scoring_service import calculate_adorescore

def analyze_feedback(text: str):
    """
    Analyze customer feedback: detect emotions, classify topics, and calculate Adorescore.
    
    Args:
        text (str): Customer feedback text.

    Returns:
        dict: Combined analysis result including emotion, topics, and Adorescore.
    """
    
    # Step 1: Predict Emotion
    emotion_result = predict_emotion(text)
    
    # Step 2: Predict Topics
    topic_result = predict_topics(text)

    # Step 3: Calculate Adorescore
    adorescore_result = calculate_adorescore(emotion_result["emotion"], topic_result["topics"])

    # Step 4: Combine results
    result = {
        "text": text,
        "emotions": emotion_result,
        "topics": topic_result,
        "adorescore": adorescore_result
    }

    return result
