import torch
from transformers import BertTokenizer, BertForSequenceClassification
from app.utils.preprocess import preprocess_text
from app.config import Config

# Load Model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)
model.load_state_dict(torch.load(Config.EMOTION_MODEL_PATH, map_location=torch.device("cpu")))
model.eval()

def predict_emotion(text: str):
    """Predict emotion from feedback text."""
    text = preprocess_text(text)
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)

    with torch.no_grad():
        outputs = model(**inputs)
        scores = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predicted_class = torch.argmax(scores, dim=-1).item()

    emotions = ["Negative", "Neutral", "Positive"]
    return {"emotion": emotions[predicted_class], "confidence": scores[0][predicted_class].item()}
