import pandas as pd

def clean_and_engineer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and engineer features for marketing analytics dataset.
    Performs the following transformations:
    - Creates 'Total_Kids' by summing 'Kidhome' and 'Teenhome' columns
    - Creates 'Total_Spend' by summing all spending category columns (wines, fruits, meat, fish, sweets, gold)
    - Creates 'Recency_Segment' by binning 'Recency' into 4 quartiles (Very recent, Recent, Not recent, Dormant)
    - Caps 'Income' values at the 99th percentile to handle outliers
    - Filters records to keep only customers aged 18-90
    - Removes rows with missing 'Income' values and resets index
    Args:
        df (pd.DataFrame): Input marketing dataset containing customer demographics and spending data
    Returns:
        pd.DataFrame: Cleaned and feature-engineered dataset with new derived features and filtered records
    """
    
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
