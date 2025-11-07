
# Kalshi Inefficiency Finder (Crypto Events)

A research-grade, Python-based project to discover and backtest mispricings in **Kalshi** binary event markets (with a focus on BTC-linked thresholds), and a stepping stone toward **Deribit** options/volatility work.

## 📌 Project Goals
- Collect Kalshi market data and related crypto features
- Model event probabilities (logistic + Monte Carlo style)
- Compare **model probability** vs **market-implied probability**
- Backtest simple trading rules based on expected value (EV)
- Produce clean visualizations and a concise report

## 🧱 Repo Structure
```
kalshi-inefficiency/
├── data/
│   ├── raw/                # Unmodified snapshots from APIs
│   └── processed/          # Cleaned, merged datasets
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_modeling.ipynb
│   └── 04_backtesting.ipynb
├── results/
│   └── plots/
├── src/
│   └── kalshi_proj/
│       ├── __init__.py
│       ├── config.py
│       ├── fetch_data.py          # Kalshi + crypto price fetchers
│       ├── preprocess.py          # Cleaning/joins/feature assembly
│       ├── visualize.py           # Plot helpers
│       ├── utils.py               # Common helpers (time, IO, logging)
│       ├── models/
│       │   ├── __init__.py
│       │   ├── logistic.py        # Logistic regression pipeline
│       │   └── mc_sim.py          # Simple Monte Carlo path sims
│       └── backtest/
│           ├── __init__.py
│           └── ev_backtester.py   # EV-based rules + P&L
├── tests/
│   ├── test_ev_backtester.py
│   └── test_preprocess.py
├── .gitignore
├── requirements.txt
├── pyproject.toml
└── LICENSE
```

## 🚀 Quickstart
```bash
# Create and activate environment (example with venv)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt

# (Optional) Install package in editable mode
pip install -e .

# Run a quick sanity check
pytest -q
```

## 🧩 Workflow
1. **Fetch** Kalshi market snapshots + BTC data -> `data/raw/`
2. **Preprocess** to tidy frames -> `data/processed/`
3. **Model** probabilities (logistic / MC) -> `notebooks/03_modeling.ipynb`
4. **Backtest** EV rules -> `src/kalshi_proj/backtest/ev_backtester.py`
5. **Visualize & report** -> `results/plots/` + README summary

## 📚 Notes
- This scaffold includes placeholders; wire in your API keys and specific endpoints.
- Keep position sizing conservative; consider Kelly-fraction or capped fixed risk.
- Later, extend to Deribit by adding an options module (pull chains, build IV smiles).

## 📝 License
MIT
