import pandas as pd
from src.data import load_data

def test_data_loading(tmp_path):
    # Create fake dataset
    file = tmp_path / "test.csv"

    df = pd.DataFrame({
        "text": ["hello", "buy now"],
        "label": [0, 1]
    })

    df.to_csv(file, index=False)

    # Load using your function
    df_loaded = load_data(file)

    assert not df_loaded.empty
