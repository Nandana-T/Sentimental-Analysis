def calculate_adorescore(emotion: str, topics: list):
    """Calculate Adorescore based on detected emotion & topics."""
    score_map = {"Positive": 100, "Neutral": 50, "Negative": 0}
    
    topic_weight = 10 * len(topics)
    base_score = score_map.get(emotion, 50)
    
    adorescore = min(base_score + topic_weight, 100)
    return {"adorescore": adorescore}
