"""Helper functions for the Wine Quality project."""

from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"

def load_wines():
    """Return red and white wine DataFrames."""
    red = pd.read_csv(DATA_DIR / "winequality-red.csv", sep=';')
    white = pd.read_csv(DATA_DIR / "winequality-white.csv", sep=';')
    return red, white
