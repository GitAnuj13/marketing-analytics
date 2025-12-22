import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))
from src.data_loader import load_data
from src.feature_engineering import clean_and_engineer
from src.eda import run_eda
from src.segmentation import run_segmentation, label_clusters, cluster_summary
from src.modeling import run_campaign_model

def main():
    df = load_data()
    df = clean_and_engineer(df)
    run_eda(df)
    df = run_segmentation(df)
    df = label_clusters(df)
    run_campaign_model(df)
    cluster_summary(df)
    print("Pipeline completed successfully")

if __name__ == "__main__":
    main()
