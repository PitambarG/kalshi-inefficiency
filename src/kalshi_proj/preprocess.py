
import pandas as pd
from .config import PATHS

def build_feature_frame() -> pd.DataFrame:
    kalshi = pd.read_csv(PATHS.data_raw / "kalshi_sample.csv")
    btc = pd.read_csv(PATHS.data_raw / "btc_sample.csv")
    # Example join; replace with real time alignment
    df = kalshi.copy()
    df['btc_price'] = btc['price'].iloc[0]
    df['time_to_expiry_days'] = 180  # placeholder
    PATHS.data_processed.mkdir(parents=True, exist_ok=True)
    df.to_csv(PATHS.data_processed / "train_features.csv", index=False)
    return df
