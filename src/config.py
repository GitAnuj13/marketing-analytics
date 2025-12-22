import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_RAW = BASE_DIR / "DATA" / "RAW" / "ifood_df.csv"
DATA_PROCESSED = BASE_DIR / "DATA" / "PROCESSED"
FIG_DIR = BASE_DIR / "FIGURES"

FIG_DIR.mkdir(exist_ok=True)
DATA_PROCESSED.mkdir(exist_ok=True)
