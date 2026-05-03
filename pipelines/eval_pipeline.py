import json
import yaml
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

df = pd.read_csv("data/golden_set.csv")

X_text = df["text"]
y = df["label"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X_text)

model = LogisticRegression()
model.fit(X, y)

preds = model.predict(X)

metrics = {
    "accuracy": accuracy_score(y, preds),
    "precision": precision_score(y, preds),
    "recall": recall_score(y, preds),
}

with open("reports/metrics.json", "w") as f:
    json.dump(metrics, f)

with open("configs/thresholds.yaml") as f:
    thresholds = yaml.safe_load(f)

for key in thresholds:
    if metrics[key] < thresholds[key]:
        raise Exception(f"{key} below threshold")

print("Evaluation passed")
