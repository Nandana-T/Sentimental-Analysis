import torch
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
from sklearn.metrics import accuracy_score, classification_report
import yaml

# Load Configurations
CONFIG_PATH = "training/config.yaml"
with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

DATASET_PATH = config["dataset_path"]
MODEL_PATH = config["emotion_model_path"]

# Load Tokenizer and Model
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)
model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device("cpu")))
model.eval()

# Load Test Data
df = pd.read_csv(DATASET_PATH)
df_test = df.sample(frac=0.2, random_state=42)  # Use 20% of data for testing

y_true, y_pred = [], []

# Make Predictions
for _, row in df_test.iterrows():
    text, label = row["text"], row["label"]
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)

    with torch.no_grad():
        outputs = model(**inputs)
        scores = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predicted_class = torch.argmax(scores, dim=-1).item()

    y_true.append(label)
    y_pred.append(predicted_class)

# Compute Metrics
accuracy = accuracy_score(y_true, y_pred)
report = classification_report(y_true, y_pred, target_names=["Negative", "Neutral", "Positive"])

print(f"📊 Accuracy: {accuracy:.4f}\n")
print(report)
