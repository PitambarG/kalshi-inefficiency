
import pandas as pd
from sklearn.linear_model import LogisticRegression

def fit_logistic(df: pd.DataFrame, y_col: str, feature_cols: list[str]) -> tuple[LogisticRegression, pd.Series]:
    X = df[feature_cols].values
    y = df[y_col].values
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    preds = pd.Series(model.predict_proba(X)[:,1], index=df.index, name="p_model")
    return model, preds
