
from pydantic import BaseModel
from pathlib import Path

class Paths(BaseModel):
    root: Path = Path(__file__).resolve().parents[2]
    data_raw: Path = root / "data" / "raw"
    data_processed: Path = root / "data" / "processed"
    results: Path = root / "results"
    plots: Path = results / "plots"

PATHS = Paths()
