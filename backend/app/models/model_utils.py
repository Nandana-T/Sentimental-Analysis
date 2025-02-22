import torch
from transformers import BertTokenizer, BertForSequenceClassification
import os

# Load Emotion Model
EMOTION_MODEL_PATH = os.path.join(os.path.dirname(__file__), "emotion_model.pth")

def load_emotion_model():
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)
    
    if os.path.exists(EMOTION_MODEL_PATH):
        model.load_state_dict(torch.load(EMOTION_MODEL_PATH, map_location=torch.device("cpu")))
    else:
        raise FileNotFoundError(f"Model file not found: {EMOTION_MODEL_PATH}")
    
    model.eval()
    return tokenizer, model
