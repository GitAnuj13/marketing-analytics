import matplotlib.pyplot as plt
import seaborn as sns
from src.config import FIG_DIR

sns.set(style="whitegrid")

def run_eda(df):
    df[["Age", "Income", "Total_Spend", "Recency"]].hist(bins=30, figsize=(12,8))
    plt.tight_layout()
    plt.savefig(FIG_DIR / "numeric_distributions.png")
    plt.close()
