from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score

def run_campaign_model(df):
    X = df[
        ["Age", "Income", "Total_Spend", "Total_Kids",
         "Recency", "NumWebPurchases", "NumCatalogPurchases",
         "NumStorePurchases", "NumWebVisitsMonth"]
    ]
    y = df["Response"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = LogisticRegression(max_iter=1000, class_weight="balanced")
    model.fit(X_train, y_train)

    print(classification_report(y_test, model.predict(X_test)))
    print("ROC-AUC:", roc_auc_score(y_test, model.predict_proba(X_test)[:,1]))

    return model
