from pathlib import Path
import pandas as pd


def ensure_output_directory():
    """Create the output directory if it doesn't exist."""
    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def validate_dataframe(df: pd.DataFrame) -> bool:
    """Check whether the dataframe contains data."""
    if df is None:
        return False

    if df.empty:
        return False

    return True


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Clean dataframe column names."""
    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    return df
