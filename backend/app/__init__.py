# app/__init__.py
from .models.model_utils import load_models

# Load AI models at startup
emotion_model, topic_model = load_models()
