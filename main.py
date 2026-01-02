"""
Sistem Analisis Data Pasien dan Tren Kesehatan
Menu utama untuk mengakses berbagai fitur analisis data pasien.
"""

import sys
from typing import Optional

from config import MENU_BORDER_LENGTH
from data_loader import (
    load_data_patients, 
    DataLoadError,
    get_unique_patients_count
)
from health_analyzer import (
    calculate_statistics,
    get_patient_summary,
    add_risk_categories,
    calculate_final_risk_category,
    get_risk_distribution,
    get_indicator_counts,
    get_daily_averages,
    get_top_risk_patients,
    get_all_statistics
)
from visualizer import (
    plot_blood_pressure_trend,
    plot_blood_sugar_trend,
    plot_cholesterol_trend,
    plot_comparison,
    plot_risk_categories,
    plot_average_indicators,
    plot_high_risk_patients
)


def print_header(title: str, width: int = MENU_BORDER_LENGTH) -> None:
    """
    Print a formatted header.
    
    Args:
        title: Title text to display.
        width: Total width of the border.
    """
    print("\n" + "=" * width)
    print(f"{title:^{width}}")
    print("=" * width)


def print_subheader(title: str, width: int = MENU_BORDER_LENGTH) -> None:
    """
    Print a formatted subheader.
    
    Args:
        title: Subheader text to display.
        width: Total width of the border.
    """
    print("\n" + "=" * width)
    print(f"{title:^{width}}")
    print("=" * width)


def show_menu() -> None:
    """Display the main menu."""
    print_header("SISTEM ANALISIS DATA PASIEN DAN TREN KESEHATAN")
    print("1. Tampilkan Ringkasan Data")
    print("2. Analisis Data Kesehatan")
    print("3. Grafik Tren Tekanan Darah")
    print("4. Grafik Tren Gula Darah")
    print("5. Grafik Tren Kolesterol")
    print("6. Grafik Perbandingan Semua Indikator")
    print("7. Kategori Risiko")
    print("8. Rata-Rata Indikator")
    print("9. Pasien Risiko Tinggi")
    print("10. Keluar")
    print("=" * MENU_BORDER_LENGTH)


def option_summary() -> None:
    """Display patient data summary."""
    try:
        df = load_data_patients()
        summary = get_patient_summary(df)
        
        print_subheader("RINGKASAN DATA PASIEN")
        print_subheader("INFORMASI DATASET")
        
        print(f"Jumlah Pasien Unik: {summary['unique_patients']}")
        print(f"Rentang Umur: {summary['min_age']} - {summary['max_age']} tahun")
        print(f"Rata-rata Umur: {summary['mean_age']:.1f} tahun")
        print(f"Total Pemeriksaan: {summary['total_examinations']} kali")
        print(f"Jumlah Kolom: {summary['total_columns']}")
    except DataLoadError as e:
        print(f"Error: {e}")


def option_health_analysis() -> None:
    """Display detailed health analysis."""
    try:
        df = load_data_patients()
        stats = calculate_statistics(df)
        
        print_subheader("ANALISIS STATISTIK KESEHATAN")
        
        print(f"Rata-rata Tekanan Darah: {stats.mean_tekanan:.2f} mmHg")
        print(f"Rata-rata Gula Darah: {stats.mean_gula:.2f} mg/dL")
        print(f"Rata-rata Kolesterol: {stats.mean_kolesterol:.2f} mg/dL")
        
        print_subheader("STATISTIK LENGKAP", 44)
        print(get_all_statistics(df))
        
        # Categorize and display risk distributions
        categorized_df = add_risk_categories(df)
        
        print_subheader("KATEGORI RISIKO BERDASARKAN TEKANAN DARAH", 41)
        print(get_indicator_counts(categorized_df, 'kategori_tekanan'))
        
        print_subheader("KATEGORI RISIKO BERDASARKAN GULA DARAH", 38)
        print(get_indicator_counts(categorized_df, 'kategori_gula'))
        
        print_subheader("KATEGORI RISIKO BERDASARKAN KOLESTEROL", 38)
        print(get_indicator_counts(categorized_df, 'kategori_kolesterol'))
    except DataLoadError as e:
        print(f"Error: {e}")


def option_blood_pressure_chart() -> None:
    """Display blood pressure trend chart."""
    try:
        df = load_data_patients()
        daily_data = get_daily_averages(df)
        plot_blood_pressure_trend(daily_data)
    except DataLoadError as e:
        print(f"Error: {e}")


def option_blood_sugar_chart() -> None:
    """Display blood sugar trend chart."""
    try:
        df = load_data_patients()
        daily_data = get_daily_averages(df)
        plot_blood_sugar_trend(daily_data)
    except DataLoadError as e:
        print(f"Error: {e}")


def option_cholesterol_chart() -> None:
    """Display cholesterol trend chart."""
    try:
        df = load_data_patients()
        daily_data = get_daily_averages(df)
        plot_cholesterol_trend(daily_data)
    except DataLoadError as e:
        print(f"Error: {e}")


def option_comparison_chart() -> None:
    """Display comparison chart for all indicators."""
    try:
        df = load_data_patients()
        daily_data = get_daily_averages(df)
        plot_comparison(daily_data)
    except DataLoadError as e:
        print(f"Error: {e}")


def option_risk_categories() -> None:
    """Display risk category pie chart."""
    try:
        df = load_data_patients()
        categorized_df = add_risk_categories(df)
        final_df = calculate_final_risk_category(categorized_df)
        risk_counts = get_risk_distribution(final_df)
        plot_risk_categories(risk_counts)
    except DataLoadError as e:
        print(f"Error: {e}")


def option_average_indicators() -> None:
    """Display average indicators bar chart."""
    try:
        df = load_data_patients()
        stats = calculate_statistics(df)
        plot_average_indicators(stats.mean_tekanan, stats.mean_gula, stats.mean_kolesterol)
    except DataLoadError as e:
        print(f"Error: {e}")


def option_high_risk_patients() -> None:
    """Display high-risk patients chart."""
    try:
        df = load_data_patients()
        top_patients = get_top_risk_patients(df)
        plot_high_risk_patients(top_patients)
    except DataLoadError as e:
        print(f"Error: {e}")


def handle_choice(choice: str) -> bool:
    """
    Handle menu choice.
    
    Args:
        choice: User's menu choice.
        
    Returns:
        bool: True if program should continue, False if should exit.
    """
    options = {
        '1': option_summary,
        '2': option_health_analysis,
        '3': option_blood_pressure_chart,
        '4': option_blood_sugar_chart,
        '5': option_cholesterol_chart,
        '6': option_comparison_chart,
        '7': option_risk_categories,
        '8': option_average_indicators,
        '9': option_high_risk_patients,
    }
    
    if choice in options:
        options[choice]()
        input("\nTekan Enter untuk melanjutkan...")
        return True
    elif choice == '10':
        print("Terima kasih telah menggunakan sistem ini. Sampai jumpa!")
        return False
    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-10.")
        return True


def main() -> None:
    """Main program loop."""
    while True:
        try:
            show_menu()
            choice = input("Pilih menu (1-10): ").strip()
            
            if not choice:
                continue
                
            if not handle_choice(choice):
                break
                
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan.")
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            input("\nTekan Enter untuk melanjutkan...")


if __name__ == "__main__":
    main()

