from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
from src.config import FIG_DIR

def run_segmentation(df, k=4):
    features = ["Income", "Age", "Total_Spend", "Total_Kids", "Recency"]
    X = df[features]

    X_scaled = StandardScaler().fit_transform(X)
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)

    df["Cluster"] = kmeans.fit_predict(X_scaled)

    sns.scatterplot(data=df, x="Income", y="Total_Spend", hue="Cluster")
    plt.savefig(FIG_DIR / "segments_income_spend.png")
    plt.close()

    return df
def label_clusters(df):
    cluster_map = {
        0: "Aspirational Spenders",
        1: "Low-Value / Entry Customers",
        2: "High-Value Loyalists",
        3: "Convenience-Oriented Shoppers"
    }

    df["Cluster_Name"] = df["Cluster"].map(cluster_map)
    return df
def cluster_summary(df):
    summary = (
        df.groupby("Cluster_Name")[[
            "Income", "Total_Spend", "Age", "Total_Kids", "Recency"
        ]]
        .mean()
        .round(1)
    )

    print("\nCluster Summary (Mean Values):")
    print(summary)

    return summary

