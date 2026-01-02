"""
Configuration module for patient data analysis system.
Contains all centralized constants, thresholds, and settings.
"""

from pathlib import Path
from typing import Final

# File Paths
DATA_FILE_PATH: Final = Path("data_pasien.csv")

# Column Names
COLUMN_ID_PASIEN: Final = "id_pasien"
COLUMN_NAMA: Final = "nama"
COLUMN_UMUR: Final = "umur"
COLUMN_JENIS_KELAMIN: Final = "jenis_kelamin"
COLUMN_TANGGAL_PERIKSA: Final = "tanggal_periksa"
COLUMN_TEKANAN_DARAH: Final = "tekanan_darah"
COLUMN_GULA_DARAH: Final = "gula_darah"
COLUMN_KOLESTEROL: Final = "kolesterol"

# Health Indicator Columns
HEALTH_COLUMNS: Final = [
    COLUMN_TEKANAN_DARAH,
    COLUMN_GULA_DARAH,
    COLUMN_KOLESTEROL,
]

# Blood Pressure Thresholds (mmHg)
TEKANAN_NORMAL_MAX: Final = 120
TEKANAN_RISIKO_TINGGI_MAX: Final = 140

# Blood Sugar Thresholds (mg/dL)
GULA_NORMAL_MAX: Final = 100
GULA_RISIKO_TINGGI_MAX: Final = 125

# Cholesterol Thresholds (mg/dL)
KOLESTEROL_NORMAL_MAX: Final = 200
KOLESTEROL_RISIKO_TINGGI_MAX: Final = 240

# Risk Categories
RISK_NORMAL: Final = "Normal"
RISK_PERLU_WASPADA: Final = "Perlu Waspada"
RISK_RISIKO_TINGGI: Final = "Risiko Tinggi"

# Category Column Names
CAT_TEKANAN: Final = "kategori_tekanan"
CAT_GULA: Final = "kategori_gula"
CAT_KOLESTEROL: Final = "kategori_kolesterol"
CAT_AKHIR: Final = "kategori_akhir"

# Visualization Settings
DEFAULT_FIGURE_SIZE: Final = (12, 6)
COMPARISON_FIGURE_SIZE: Final = (15, 7)
TOP_PATIENTS_COUNT: Final = 5
BAR_WIDTH: Final = 0.25

# Colors
COLOR_TEKANAN: Final = "red"
COLOR_GULA: Final = "green"
COLOR_KOLESTEROL: Final = "blue"

# UI Settings
MENU_BORDER_LENGTH: Final = 60
MENU_INNER_BORDER_LENGTH: Final = 36
MENU_INNER_BORDER_LENGTH_2: Final = 41
MENU_INNER_BORDER_LENGTH_3: Final = 44
MENU_INNER_BORDER_LENGTH_4: Final = 92

