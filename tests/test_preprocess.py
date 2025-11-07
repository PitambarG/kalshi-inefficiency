
from src.kalshi_proj.preprocess import build_feature_frame

def test_build_feature_frame_smoke(tmp_path, monkeypatch):
    # Just ensure function returns a DataFrame
    df = build_feature_frame()
    assert not df.empty
