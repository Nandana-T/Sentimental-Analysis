import pandas as pd
import re
import json

# File paths
DATASET_PATH = "data/dataset.csv"
PROCESSED_CSV_PATH = "data/processed_feedback.csv"
PROCESSED_JSON_PATH = "data/processed_feedback.json"

# Emotion Label Mapping
emotion_map = {"Negative": 0, "Neutral": 1, "Positive": 2}

def clean_text(text):
    """Clean and preprocess text."""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    return text.strip()

def process_dataset():
    """Load, clean, and process the dataset."""
    print("📂 Loading dataset...")
    df = pd.read_csv(DATASET_PATH)

    print("🧹 Cleaning text...")
    df["text"] = df["text"].apply(clean_text)

    print("🔢 Encoding emotion labels...")
    df["label"] = df["emotion"].map(emotion_map)

    print("🗂️ Processing topics...")
    df["topics"] = df["topics"].apply(lambda x: x.split(",") if isinstance(x, str) else [])

    # Save Processed Data (CSV)
    df.to_csv(PROCESSED_CSV_PATH, index=False)
    print(f"✅ Processed dataset saved as {PROCESSED_CSV_PATH}")

    # Save Processed Data (JSON)
    df.to_json(PROCESSED_JSON_PATH, orient="records", indent=4)
    print(f"✅ Processed dataset saved as {PROCESSED_JSON_PATH}")

if __name__ == "__main__":
    process_dataset()
