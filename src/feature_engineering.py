import pandas as pd

def clean_and_engineer(df: pd.DataFrame) -> pd.DataFrame:
    
    df["Total_Kids"] = df["Kidhome"] + df["Teenhome"]

    spend_cols = [
        "MntWines", "MntFruits", "MntMeatProducts",
        "MntFishProducts", "MntSweetProducts", "MntGoldProds"
    ]
    df["Total_Spend"] = df[spend_cols].sum(axis=1)

    df["Recency_Segment"] = pd.qcut(
        df["Recency"], 4,
        labels=["Very recent", "Recent", "Not recent", "Dormant"]
    )

    income_cap = df["Income"].quantile(0.99)
    df.loc[df["Income"] > income_cap, "Income"] = income_cap

    df = df[(df["Age"] >= 18) & (df["Age"] <= 90)]
    df = df.dropna(subset=["Income"]).reset_index(drop=True)

    return df
