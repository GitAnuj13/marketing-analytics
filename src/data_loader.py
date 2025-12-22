import pandas as pd
from src.config import DATA_RAW

def load_data():
    df = pd.read_csv(DATA_RAW)
    print("Loaded data:", df.shape)
    return df
