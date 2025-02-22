import re

def preprocess_text(text: str):
    """Clean and preprocess text."""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.strip()
