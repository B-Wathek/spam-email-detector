from sklearn.metrics import classification_report
import joblib

def evaluate(X_test, y_test):
    vectorizer, model = joblib.load("model.joblib")
    preds = model.predict(vectorizer.transform(X_test))

    report = classification_report(y_test, preds)

    with open("reports/eval_report.md", "w") as f:
        f.write(report)
