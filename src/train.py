from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

from data import load_data
from model import build_model

def train():
    df = load_data("data/spam.csv")

    X_train, X_test, y_train, y_test = train_test_split(
        df['text'], df['label'], test_size=0.2
    )

    vectorizer, model = build_model()

    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model.fit(X_train_vec, y_train)

    preds = model.predict(X_test_vec)
    acc = accuracy_score(y_test, preds)

    joblib.dump((vectorizer, model), "model.joblib")

    print(f"Accuracy: {acc}")

if __name__ == "__main__":
    train()
