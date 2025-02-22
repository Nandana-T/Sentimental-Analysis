import torch
from transformers import BertTokenizer, BertForSequenceClassification

class EmotionModel:
    """A PyTorch model for classifying customer emotions."""
    
    def __init__(self, model_path="backend/models/emotion_model.pth"):
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)
        self.model.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
        self.model.eval()  # Set model to evaluation mode

    def predict(self, text):
        """Predict emotion from text input."""
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
        
        with torch.no_grad():
            outputs = self.model(**inputs)
            scores = torch.nn.functional.softmax(outputs.logits, dim=-1)
            predicted_class = torch.argmax(scores, dim=-1).item()

        emotions = ["Negative", "Neutral", "Positive"]
        return {"emotion": emotions[predicted_class], "confidence": scores[0][predicted_class].item()}
