from transformers import pipeline
import pandas as pd
import yaml
import json

# Load Configurations
CONFIG_PATH = "training/config.yaml"
with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

DATASET_PATH = config["dataset_path"]
TOPIC_MODEL_OUTPUT = config["topic_model_output"]

# Load Dataset
df = pd.read_csv(DATASET_PATH)

# Define Candidate Topics
candidate_labels = ["Delivery", "Quality", "Customer Service", "Price", "Product Features"]

# Load Zero-Shot Classifier
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Predict Topics
predictions = []
for text in df["text"]:
    result = classifier(text, candidate_labels)
    predictions.append({"text": text, "topics": result["labels"], "scores": result["scores"]})

# Save Predictions
with open(TOPIC_MODEL_OUTPUT, "w") as f:
    json.dump(predictions, f, indent=4)

print(f"✅ Topic model output saved to {TOPIC_MODEL_OUTPUT}")
