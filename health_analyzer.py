"""
Health analysis module for patient data.
Provides functions for analyzing patient health indicators and risk categories.
"""

import pandas as pd
import numpy as np
from typing import Dict, Tuple, List
from dataclasses import dataclass

import config as cfg


@dataclass
class HealthStatistics:
    """Data class to hold health statistics."""
    mean_tekanan: float
    mean_gula: float
    mean_kolesterol: float
    std_tekanan: float
    std_gula: float
    std_kolesterol: float


def categorize_tekanan_darah(value: float) -> str:
    """
    Categorize blood pressure value into risk level.
    
    Args:
        value: Blood pressure value in mmHg.
        
    Returns:
        str: Risk category (Normal, Perlu Waspada, or Risiko Tinggi).
    """
    if value > cfg.TEKANAN_RISIKO_TINGGI_MAX:
        return cfg.RISK_RISIKO_TINGGI
    elif value >= cfg.TEKANAN_NORMAL_MAX:
        return cfg.RISK_PERLU_WASPADA
    return cfg.RISK_NORMAL


def categorize_gula_darah(value: float) -> str:
    """
    Categorize blood sugar value into risk level.
    
    Args:
        value: Blood sugar value in mg/dL.
        
    Returns:
        str: Risk category (Normal, Perlu Waspada, or Risiko Tinggi).
    """
    if value > cfg.GULA_RISIKO_TINGGI_MAX:
        return cfg.RISK_RISIKO_TINGGI
    elif value >= cfg.GULA_NORMAL_MAX:
        return cfg.RISK_PERLU_WASPADA
    return cfg.RISK_NORMAL


def categorize_kolesterol(value: float) -> str:
    """
    Categorize cholesterol value into risk level.
    
    Args:
        value: Cholesterol value in mg/dL.
        
    Returns:
        str: Risk category (Normal, Perlu Waspada, or Risiko Tinggi).
    """
    if value > cfg.KOLESTEROL_RISIKO_TINGGI_MAX:
        return cfg.RISK_RISIKO_TINGGI
    elif value >= cfg.KOLESTEROL_NORMAL_MAX:
        return cfg.RISK_PERLU_WASPADA
    return cfg.RISK_NORMAL


def calculate_statistics(df: pd.DataFrame) -> HealthStatistics:
    """
    Calculate statistics for all health indicators.
    
    Args:
        df: Patient DataFrame.
        
    Returns:
        HealthStatistics: Object containing mean and std values.
    """
    return HealthStatistics(
        mean_tekanan=df[cfg.COLUMN_TEKANAN_DARAH].mean(),
        mean_gula=df[cfg.COLUMN_GULA_DARAH].mean(),
        mean_kolesterol=df[cfg.COLUMN_KOLESTEROL].mean(),
        std_tekanan=df[cfg.COLUMN_TEKANAN_DARAH].std(),
        std_gula=df[cfg.COLUMN_GULA_DARAH].std(),
        std_kolesterol=df[cfg.COLUMN_KOLESTEROL].std(),
    )


def get_patient_summary(df: pd.DataFrame) -> Dict[str, int]:
    """
    Get summary statistics about the patient dataset.
    
    Args:
        df: Patient DataFrame.
        
    Returns:
        Dict containing patient summary statistics.
    """
    return {
        "unique_patients": df[cfg.COLUMN_ID_PASIEN].nunique(),
        "min_age": df[cfg.COLUMN_UMUR].min(),
        "max_age": df[cfg.COLUMN_UMUR].max(),
        "mean_age": df[cfg.COLUMN_UMUR].mean(),
        "total_examinations": len(df),
        "total_columns": df.shape[1],
    }


def add_risk_categories(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add risk category columns to the DataFrame without modifying original.
    
    Args:
        df: Patient DataFrame.
        
    Returns:
        pd.DataFrame: New DataFrame with added category columns.
    """
    result_df = df.copy()
    
    result_df[cfg.CAT_TEKANAN] = result_df[cfg.COLUMN_TEKANAN_DARAH].apply(
        categorize_tekanan_darah
    )
    result_df[cfg.CAT_GULA] = result_df[cfg.COLUMN_GULA_DARAH].apply(
        categorize_gula_darah
    )
    result_df[cfg.CAT_KOLESTEROL] = result_df[cfg.COLUMN_KOLESTEROL].apply(
        categorize_kolesterol
    )
    
    return result_df


def calculate_final_risk_category(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate overall risk category based on all indicators.
    
    The final category is determined by the highest risk level:
    - If any indicator is "Risiko Tinggi" → Risiko Tinggi
    - If any indicator is "Perlu Waspada" → Perlu Waspada
    - Otherwise → Normal
    
    Args:
        df: Patient DataFrame with risk category columns.
        
    Returns:
        pd.DataFrame: DataFrame with final risk category added.
    """
    result_df = df.copy()
    result_df[cfg.CAT_AKHIR] = cfg.RISK_NORMAL
    
    # Check for high risk first (takes priority)
    kondisi_tinggi = (
        (result_df[cfg.CAT_TEKANAN] == cfg.RISK_RISIKO_TINGGI) |
        (result_df[cfg.CAT_GULA] == cfg.RISK_RISIKO_TINGGI) |
        (result_df[cfg.CAT_KOLESTEROL] == cfg.RISK_RISIKO_TINGGI)
    )
    result_df.loc[kondisi_tinggi, cfg.CAT_AKHIR] = cfg.RISK_RISIKO_TINGGI
    
    # Check for warning
    kondisi_waspada = (
        (result_df[cfg.CAT_TEKANAN] == cfg.RISK_PERLU_WASPADA) |
        (result_df[cfg.CAT_GULA] == cfg.RISK_PERLU_WASPADA) |
        (result_df[cfg.CAT_KOLESTEROL] == cfg.RISK_PERLU_WASPADA)
    )
    result_df.loc[kondisi_waspada, cfg.CAT_AKHIR] = cfg.RISK_PERLU_WASPADA
    
    return result_df


def get_risk_distribution(df: pd.DataFrame) -> pd.Series:
    """
    Get the distribution of risk categories.
    
    Args:
        df: Patient DataFrame with final risk category.
        
    Returns:
        pd.Series: Count of patients in each risk category.
    """
    return df.groupby(cfg.CAT_AKHIR)[cfg.COLUMN_ID_PASIEN].count()


def get_indicator_counts(
    df: pd.DataFrame, 
    category_column: str
) -> pd.Series:
    """
    Get count of patients per indicator category.
    
    Args:
        df: Patient DataFrame.
        category_column: Name of the category column to count.
        
    Returns:
        pd.Series: Count of patients in each category.
    """
    return df.groupby(category_column)[cfg.COLUMN_ID_PASIEN].count()


def get_daily_averages(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate daily averages for all health indicators.
    
    Args:
        df: Patient DataFrame.
        
    Returns:
        pd.DataFrame: Daily averages indexed by date.
    """
    return df.groupby(cfg.COLUMN_TANGGAL_PERIKSA)[
        [cfg.COLUMN_TEKANAN_DARAH, cfg.COLUMN_GULA_DARAH, cfg.COLUMN_KOLESTEROL]
    ].mean()


def get_top_risk_patients(
    df: pd.DataFrame, 
    n: int = cfg.TOP_PATIENTS_COUNT
) -> pd.DataFrame:
    """
    Get top N patients with highest blood pressure.
    
    Args:
        df: Patient DataFrame.
        n: Number of patients to return.
        
    Returns:
        pd.DataFrame: Top N patients sorted by blood pressure.
    """
    pasien_stats = df.groupby(cfg.COLUMN_NAMA)[
        [cfg.COLUMN_TEKANAN_DARAH, cfg.COLUMN_GULA_DARAH, cfg.COLUMN_KOLESTEROL]
    ].mean()
    
    return pasien_stats.sort_values(
        cfg.COLUMN_TEKANAN_DARAH, 
        ascending=False
    ).head(n)


def get_all_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get complete statistics for health indicators.
    
    Args:
        df: Patient DataFrame.
        
    Returns:
        pd.DataFrame: Descriptive statistics.
    """
    return df[cfg.HEALTH_COLUMNS].describe()

