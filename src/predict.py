import joblib

def predict(text):
    vectorizer, model = joblib.load("model.joblib")
    X = vectorizer.transform([text])
    return model.predict(X)[0]
