import torch
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from torch.utils.data import Dataset
import os
import yaml

# Load Configurations
CONFIG_PATH = "training/config.yaml"
with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f)

DATASET_PATH = config["dataset_path"]
MODEL_SAVE_PATH = config["emotion_model_path"]

# Define Dataset Class
class EmotionDataset(Dataset):
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.texts = self.data["text"].tolist()
        self.labels = self.data["label"].tolist()

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        encoding = tokenizer(self.texts[idx], truncation=True, padding="max_length", max_length=128, return_tensors="pt")
        return {key: val.squeeze(0) for key, val in encoding.items()}, torch.tensor(self.labels[idx])

# Load Dataset
dataset = EmotionDataset(DATASET_PATH)

# Load Pretrained Model
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=3)

# Training Arguments
training_args = TrainingArguments(
    output_dir=config["output_dir"],
    num_train_epochs=config["epochs"],
    per_device_train_batch_size=config["batch_size"],
    per_device_eval_batch_size=config["batch_size"],
    logging_dir=config["logging_dir"],
    evaluation_strategy="epoch",
    save_strategy="epoch"
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)

# Train Model
trainer.train()

# Save Model
os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)
torch.save(model.state_dict(), MODEL_SAVE_PATH)
print(f"✅ Model saved to {MODEL_SAVE_PATH}")
