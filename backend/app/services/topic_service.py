from transformers import pipeline
from app.utils.preprocess import preprocess_text

topic_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def predict_topics(text: str):
    """Predict topics in feedback."""
    text = preprocess_text(text)
    candidate_labels = ["Delivery", "Quality", "Customer Service", "Price", "Product Features"]
    
    result = topic_classifier(text, candidate_labels)
    return {"topics": result["labels"], "scores": result["scores"]}
