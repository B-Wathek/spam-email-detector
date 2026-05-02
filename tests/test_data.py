from src.data import load_data

def test_data_loading():
    df = load_data("data/spam.csv")
    assert not df.empty
