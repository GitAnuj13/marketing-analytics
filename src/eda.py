import matplotlib.pyplot as plt
import seaborn as sns
from src.config import FIG_DIR

sns.set(style="whitegrid")

import matplotlib.pyplot as plt
import seaborn as sns
from src.config import FIG_DIR

sns.set(style="whitegrid")

def run_eda(df):
    """
    Runs full EDA and saves all figures to disk.
    """

    # 1. Numeric distributions
    df[["Age", "Income", "Total_Spend", "Recency"]].hist(
        bins=30, figsize=(12, 8)
    )
    plt.suptitle("Numeric Feature Distributions")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "numeric_distributions.png")
    plt.close()

    # 2. Spend by product
    spend_cols = [
        "MntWines", "MntFruits", "MntMeatProducts",
        "MntFishProducts", "MntSweetProducts", "MntGoldProds"
    ]
    avg_spend = df[spend_cols].mean().sort_values(ascending=False)

    plt.figure(figsize=(8, 4))
    sns.barplot(x=avg_spend.index, y=avg_spend.values)
    plt.xticks(rotation=45)
    plt.title("Average Spend by Product Category")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "avg_spend_products.png")
    plt.close()

    # 3. Channel usage
    channel_cols = [
        "NumWebPurchases", "NumCatalogPurchases", "NumStorePurchases"
    ]
    df[channel_cols].mean().plot(kind="bar", figsize=(6, 4))
    plt.title("Average Channel Usage")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "channel_usage.png")
    plt.close()

    # 4. Campaign response (if exists)
    
    plt.figure(figsize=(6, 4))
    sns.boxplot(data=df, x="Response", y="Total_Spend")
    plt.title("Spend vs Campaign Response")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "spend_vs_response.png")
    plt.close()

    print("EDA completed. Figures saved to:", FIG_DIR)

