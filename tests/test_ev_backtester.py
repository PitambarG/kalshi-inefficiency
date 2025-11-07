
from src.kalshi_proj.backtest.ev_backtester import expected_value

def test_expected_value():
    assert expected_value(0.60, 0.55) == 0.05
