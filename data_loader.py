"""
Data loading module for patient data analysis system.
Provides caching, error handling, and type-safe data loading.
"""

import pandas as pd
from functools import lru_cache
from pathlib import Path
from typing import Optional

from config import DATA_FILE_PATH


class DataLoadError(Exception):
    """Custom exception for data loading errors."""
    pass


@lru_cache(maxsize=1)
def load_data_patients(file_path: Optional[str] = None) -> pd.DataFrame:
    """
    Load patient data from CSV file with caching support.
    
    Uses LRU cache to avoid reloading the same file multiple times.
    This improves performance when the data is accessed frequently.
    
    Args:
        file_path: Optional path to the CSV file. Defaults to DATA_FILE_PATH.
        
    Returns:
        pd.DataFrame: Loaded patient data.
        
    Raises:
        DataLoadError: If the file cannot be loaded or is invalid.
    """
    path = Path(file_path) if file_path else DATA_FILE_PATH
    
    try:
        df = pd.read_csv(path)
        _validate_dataframe(df)
        return df
    except FileNotFoundError:
        raise DataLoadError(f"Data file not found: {path}")
    except pd.errors.EmptyDataError:
        raise DataLoadError(f"Data file is empty: {path}")
    except pd.errors.ParserError as e:
        raise DataLoadError(f"Error parsing CSV file: {e}")
    except Exception as e:
        raise DataLoadError(f"Unexpected error loading data: {e}")


def _validate_dataframe(df: pd.DataFrame) -> None:
    """
    Validate that the DataFrame contains required columns.
    
    Args:
        df: DataFrame to validate.
        
    Raises:
        DataLoadError: If required columns are missing.
    """
    required_columns = {
        "id_pasien", "nama", "umur", "jenis_kelamin",
        "tanggal_periksa", "tekanan_darah", "gula_darah", "kolesterol"
    }
    
    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise DataLoadError(f"Missing required columns: {missing_columns}")


def load_data_with_date_filter(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None
) -> pd.DataFrame:
    """
    Load patient data with optional date filtering.
    
    Args:
        start_date: Filter records from this date (YYYY-MM-DD format).
        end_date: Filter records until this date (YYYY-MM-DD format).
        
    Returns:
        pd.DataFrame: Filtered patient data.
    """
    df = load_data_patients()
    
    if start_date:
        df = df[df["tanggal_periksa"] >= start_date]
    if end_date:
        df = df[df["tanggal_periksa"] <= end_date]
    
    return df


def get_unique_patients_count(df: pd.DataFrame) -> int:
    """
    Get the count of unique patients in the dataset.
    
    Args:
        df: Patient DataFrame.
        
    Returns:
        int: Number of unique patients.
    """
    return df["id_pasien"].nunique()


def clear_cache() -> None:
    """Clear the data cache to allow reloading from file."""
    load_data_patients.cache_clear()

