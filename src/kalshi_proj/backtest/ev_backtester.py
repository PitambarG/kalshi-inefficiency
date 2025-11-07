
import pandas as pd

def expected_value(p_model: float, p_market: float) -> float:
    """EV per $1 contract on a YES outcome."""
    return p_model - p_market

def simple_rule_signals(df: pd.DataFrame, p_model_col: str, p_market_col: str, buy_thresh=0.05, sell_thresh=-0.05) -> pd.DataFrame:
    df = df.copy()
    ev = df[p_model_col] - df[p_market_col]
    df['ev'] = ev
    df['signal'] = 0
    df.loc[ev >= buy_thresh, 'signal'] = 1   # buy YES
    df.loc[ev <= sell_thresh, 'signal'] = -1 # buy NO
    return df

def pnl_from_outcomes(df: pd.DataFrame, signal_col: str, outcome_col: str) -> pd.DataFrame:
    """Outcome is 1 if event happens else 0. Signal: 1=YES, -1=NO, 0=flat."""
    df = df.copy()
    pnl = []
    for sig, outcome, p_yes in zip(df[signal_col], df[outcome_col], df['p_market']):
        if sig == 1:
            pnl.append(1 - p_yes if outcome==1 else -p_yes)
        elif sig == -1:
            p_no = 1 - p_yes
            pnl.append(1 - p_no if outcome==0 else -p_no)
        else:
            pnl.append(0.0)
    df['pnl'] = pnl
    return df
