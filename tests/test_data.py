import pandas as pd

# Load dataset
df = pd.read_csv("data/spam.csv")

# --------------------
# 1–3 Syntactic checks
# --------------------

def test_no_null_text():
    assert df["text"].isnull().sum() == 0

def test_no_empty_strings():
    assert (df["text"] == "").sum() == 0

def test_labels_valid():
    assert set(df["label"].unique()).issubset({0, 1})

# --------------------
# 4–7 Structural checks
# --------------------

def test_no_duplicates():
    assert df.duplicated().sum() == 0

def test_row_alignment():
    assert len(df["text"]) == len(df["label"])

def test_no_leakage():
    assert not df["text"].str.contains("label", case=False).any()

def test_dataset_min_size():
    assert len(df) >= 10

# --------------------
# 8–10 Statistical checks
# --------------------

def test_class_balance():
    ratio = df["label"].mean()
    assert 0.2 <= ratio <= 0.8

def test_text_variance():
    assert df["text"].str.len().std() > 0

def test_label_distribution():
    assert df["label"].value_counts().min() > 0
