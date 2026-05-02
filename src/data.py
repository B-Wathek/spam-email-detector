import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df = df[['text', 'label']]
    df.dropna(inplace=True)
    return df
