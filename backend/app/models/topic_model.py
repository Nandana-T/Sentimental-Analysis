from transformers import pipeline

class TopicModel:
    """A BART-based model for classifying topics in customer feedback."""
    
    def __init__(self):
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    def predict(self, text):
        """Predict topics from text input."""
        candidate_labels = ["Delivery", "Quality", "Customer Service", "Price", "Product Features"]
        result = self.classifier(text, candidate_labels)
        return {"topics": result["labels"], "scores": result["scores"]}
