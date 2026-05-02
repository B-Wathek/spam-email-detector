from src.model import build_model

def test_model_creation():
    vectorizer, model = build_model()
    assert model is not None
