"""
Visualization module for patient data analysis.
Provides functions to create various charts and graphs.
"""

import matplotlib.pyplot as plt
import pandas as pd
import config as cfg

def setup_plot(
    title: str, 
    xlabel: str, 
    ylabel: str,
    figsize: tuple = cfg.DEFAULT_FIGURE_SIZE
) -> plt.Figure:
    """
    Create a configured plot with standard settings.
    
    Args:
        title: Plot title.
        xlabel: X-axis label.
        ylabel: Y-axis label.
        figsize: Figure size tuple.
        
    Returns:
        plt.Figure: Configured matplotlib figure.
    """
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.grid(True, alpha=0.3)
    return fig


def plot_blood_pressure_trend(daily_data: pd.DataFrame) -> None:
    """
    Create a line chart for blood pressure trends.
    
    Args:
        daily_data: DataFrame with daily averages.
    """
    plt.figure(figsize=cfg.DEFAULT_FIGURE_SIZE)
    plt.plot(
        daily_data.index, 
        daily_data[cfg.COLUMN_TEKANAN_DARAH],
        marker='o', 
        linewidth=2, 
        markersize=8, 
        color=cfg.COLOR_TEKANAN
    )
    plt.title('Grafik Tren Tekanan Darah', fontsize=16, fontweight='bold')
    plt.xlabel('Tanggal Pemeriksaan', fontsize=12)
    plt.ylabel('Rata-rata Tekanan Darah (mmHg)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("\nGrafik Tren Tekanan Darah telah ditampilkan!")


def plot_blood_sugar_trend(daily_data: pd.DataFrame) -> None:
    """
    Create a line chart for blood sugar trends.
    
    Args:
        daily_data: DataFrame with daily averages.
    """
    plt.figure(figsize=cfg.DEFAULT_FIGURE_SIZE)
    plt.plot(
        daily_data.index, 
        daily_data[cfg.COLUMN_GULA_DARAH],
        marker='s', 
        linewidth=2, 
        markersize=8, 
        color=cfg.COLOR_GULA
    )
    plt.title('Grafik Tren Gula Darah', fontsize=16, fontweight='bold')
    plt.xlabel('Tanggal Pemeriksaan', fontsize=12)
    plt.ylabel('Rata-rata Gula Darah (mg/dL)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("\nGrafik Tren Gula Darah telah ditampilkan!")


def plot_cholesterol_trend(daily_data: pd.DataFrame) -> None:
    """
    Create a line chart for cholesterol trends.
    
    Args:
        daily_data: DataFrame with daily averages.
    """
    plt.figure(figsize=cfg.DEFAULT_FIGURE_SIZE)
    plt.plot(
        daily_data.index, 
        daily_data[cfg.COLUMN_KOLESTEROL],
        marker='^', 
        linewidth=2, 
        markersize=8, 
        color=cfg.COLOR_KOLESTEROL
    )
    plt.title('Grafik Tren Kolesterol', fontsize=16, fontweight='bold')
    plt.xlabel('Tanggal Pemeriksaan', fontsize=12)
    plt.ylabel('Rata-rata Kolesterol (mg/dL)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("\nGrafik Tren Kolesterol telah ditampilkan!")


def plot_comparison(daily_data: pd.DataFrame) -> None:
    """
    Create a comparison plot with all three indicators.
    
    Args:
        daily_data: DataFrame with daily averages for all indicators.
    """
    plt.figure(figsize=cfg.COMPARISON_FIGURE_SIZE)
    
    # Blood pressure subplot
    plt.subplot(3, 1, 1)
    plt.plot(
        daily_data.index, 
        daily_data[cfg.COLUMN_TEKANAN_DARAH],
        marker='o', 
        linewidth=2, 
        markersize=6, 
        color=cfg.COLOR_TEKANAN
    )
    plt.title('Grafik Tren Tekanan Darah', fontsize=14, fontweight='bold')
    plt.ylabel('Tekanan Darah (mmHg)', fontsize=11)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    # Blood sugar subplot
    plt.subplot(3, 1, 2)
    plt.plot(
        daily_data.index, 
        daily_data[cfg.COLUMN_GULA_DARAH],
        marker='s', 
        linewidth=2, 
        markersize=6, 
        color=cfg.COLOR_GULA
    )
    plt.title('Grafik Tren Gula Darah', fontsize=14, fontweight='bold')
    plt.ylabel('Gula Darah (mg/dL)', fontsize=11)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    # Cholesterol subplot
    plt.subplot(3, 1, 3)
    plt.plot(
        daily_data.index, 
        daily_data[cfg.COLUMN_KOLESTEROL],
        marker='^', 
        linewidth=2, 
        markersize=6, 
        color=cfg.COLOR_KOLESTEROL
    )
    plt.title('Grafik Tren Kolesterol', fontsize=14, fontweight='bold')
    plt.xlabel('Tanggal Pemeriksaan', fontsize=11)
    plt.ylabel('Kolesterol (mg/dL)', fontsize=11)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    print("\nGrafik Perbandingan Semua Indikator telah ditampilkan!")


def plot_risk_categories(risk_counts: pd.Series) -> None:
    """
    Create a pie chart for risk category distribution.
    
    Args:
        risk_counts: Series with risk category counts.
    """
    plt.figure(figsize=(10, 8))
    
    colors = [cfg.RISK_NORMAL, cfg.RISK_PERLU_WASPADA, cfg.RISK_RISIKO_TINGGI]
    color_map = {
        cfg.RISK_NORMAL: 'green',
        cfg.RISK_PERLU_WASPADA: 'orange',
        cfg.RISK_RISIKO_TINGGI: 'red'
    }
    actual_colors = [
        color_map.get(cat, 'gray') for cat in risk_counts.index
    ]
    
    explode = [0.1 if cat == cfg.RISK_RISIKO_TINGGI else 0 for cat in risk_counts.index]
    
    plt.pie(
        risk_counts.values, 
        labels=risk_counts.index, 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=actual_colors, 
        explode=explode, 
        shadow=True, 
        textprops={'fontsize': 12}
    )
    plt.title('Kategori Risiko Kesehatan Pasien', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.show()
    print("\nKategori Risiko Kesehatan Pasien telah ditampilkan!")


def plot_average_indicators(
    avg_tekanan: float, 
    avg_gula: float, 
    avg_kolesterol: float
) -> None:
    """
    Create a bar chart for average health indicators.
    
    Args:
        avg_tekanan: Average blood pressure.
        avg_gula: Average blood sugar.
        avg_kolesterol: Average cholesterol.
    """
    plt.figure(figsize=(10, 6))
    
    indikator = ['Tekanan Darah', 'Gula Darah', 'Kolesterol']
    nilai = [avg_tekanan, avg_gula, avg_kolesterol]
    warna = [cfg.COLOR_TEKANAN, cfg.COLOR_GULA, cfg.COLOR_KOLESTEROL]
    
    bars = plt.bar(indikator, nilai, color=warna, alpha=0.7, edgecolor='black', linewidth=1.5)
    
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2., 
            height,
            f'{height:.2f}',
            ha='center', 
            va='bottom', 
            fontsize=12, 
            fontweight='bold'
        )
    
    plt.title('Rata-Rata Indikator Kesehatan Pasien', fontsize=16, fontweight='bold')
    plt.ylabel('Nilai Rata-Rata', fontsize=12)
    plt.xlabel('Indikator Kesehatan', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("\nRata-Rata Indikator Kesehatan Pasien telah ditampilkan!")


def plot_high_risk_patients(top_patients: pd.DataFrame) -> None:
    """
    Create a grouped bar chart for top high-risk patients.
    
    Args:
        top_patients: DataFrame with top patients and their averages.
    """
    plt.figure(figsize=cfg.DEFAULT_FIGURE_SIZE)
    
    x = range(len(top_patients))
    width = cfg.BAR_WIDTH
    
    plt.bar(
        [i - width for i in x], 
        top_patients[cfg.COLUMN_TEKANAN_DARAH], 
        width=width, 
        label='Tekanan Darah', 
        color=cfg.COLOR_TEKANAN, 
        alpha=0.7
    )
    plt.bar(
        x, 
        top_patients[cfg.COLUMN_GULA_DARAH], 
        width=width, 
        label='Gula Darah', 
        color=cfg.COLOR_GULA, 
        alpha=0.7
    )
    plt.bar(
        [i + width for i in x], 
        top_patients[cfg.COLUMN_KOLESTEROL], 
        width=width, 
        label='Kolesterol', 
        color=cfg.COLOR_KOLESTEROL, 
        alpha=0.7
    )
    
    plt.xlabel('Nama Pasien', fontsize=12)
    plt.ylabel('Nilai Indikator', fontsize=12)
    plt.title('Pasien Risiko Tertinggi', fontsize=16, fontweight='bold')
    plt.xticks(x, top_patients.index, rotation=45)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()
    print("\nPasien Risiko Tertinggi telah ditampilkan!")

