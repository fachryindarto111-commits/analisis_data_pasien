
from functools import cache
import pandas as pd
import matplotlib.pyplot as plt

@cache
def load_data_pasients():
    df = pd.read_csv('data_pasien.csv')
    return df


def tampilkan_menu():
    print("\n" + "="*60)
    print("      SISTEM ANALISIS DATA PASIEN DAN TREN KESEHATAN")
    print("="*60)
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
    print("="*60)

def ringkasan_data():
    df =load_data_pasients()
    
    print("\n" + "="*92)
    print("                                    RINGKASAN DATA PASIEN")
    print("="*92)
    
    print("\n" + "="*92)
    print("                                     INFORMASI DATASET")
    print("="*92)
    jumlah_pasien_unik = df['id_pasien'].nunique()
    umur_min = df['umur'].min()
    umur_max = df['umur'].max()
    umur_rata = df['umur'].mean()
    
    print(f"Jumlah Pasien Unik: {jumlah_pasien_unik}")
    print(f"Rentang Umur: {umur_min} - {umur_max} tahun")
    print(f"Rata-rata Umur: {umur_rata:.1f} tahun")
    print(f"Total Pemeriksaan: {df.shape[0]} kali")
    print(f"Jumlah Kolom: {df.shape[1]}")

def analisis_kesehatan():
    df =load_data_pasients()
    
    print("\n" + "="*36)
    print("    ANALISIS STATISTIK KESEHATAN")
    print("="*36)
    
    rata_tekanan = df['tekanan_darah'].mean()
    print(f"Rata-rata Tekanan Darah: {rata_tekanan:.2f} mmHg")
    
    rata_gula = df['gula_darah'].mean()
    print(f"Rata-rata Gula Darah: {rata_gula:.2f} mg/dL")
    
    rata_kolesterol = df['kolesterol'].mean()
    print(f"Rata-rata Kolesterol: {rata_kolesterol:.2f} mg/dL")
    
    print("\n" + "="*44)
    print("             STATISTIK LENGKAP")
    print("="*44)
    print(df[['tekanan_darah', 'gula_darah', 'kolesterol']].describe())
    
    df['kategori_tekanan'] = 'Normal'
    df.loc[df['tekanan_darah'] >= 120, 'kategori_tekanan'] = 'Perlu Waspada'
    df.loc[df['tekanan_darah'] > 140, 'kategori_tekanan'] = 'Risiko Tinggi'
    
    df['kategori_gula'] = 'Normal'
    df.loc[df['gula_darah'] >= 100, 'kategori_gula'] = 'Perlu Waspada'
    df.loc[df['gula_darah'] > 125, 'kategori_gula'] = 'Risiko Tinggi'
    
    df['kategori_kolesterol'] = 'Normal'
    df.loc[df['kolesterol'] >= 200, 'kategori_kolesterol'] = 'Perlu Waspada'
    df.loc[df['kolesterol'] > 240, 'kategori_kolesterol'] = 'Risiko Tinggi'
    
    print("\n" + "="*41)
    print("KATEGORI RISIKO BERDASARKAN TEKANAN DARAH")
    print("="*41)
    print(df.groupby('kategori_tekanan')['id_pasien'].count())
    
    print("\n" + "="*38)
    print("KATEGORI RISIKO BERDASARKAN GULA DARAH")
    print("="*38)
    print(df.groupby('kategori_gula')['id_pasien'].count())
    
    print("\n" + "="*38)
    print("KATEGORI RISIKO BERDASARKAN KOLESTEROL")
    print("="*38)
    print(df.groupby('kategori_kolesterol')['id_pasien'].count())

def grafik_tekanan_darah():
    df =load_data_pasients()
    tekanan_harian = df.groupby('tanggal_periksa')['tekanan_darah'].mean()
    
    plt.figure(figsize=(12, 6))
    plt.plot(tekanan_harian.index, tekanan_harian.values, marker='o', linewidth=2, markersize=8, color='red')
    plt.title('Grafik Tren Tekanan Darah', fontsize=16, fontweight='bold')
    plt.xlabel('Tanggal Pemeriksaan', fontsize=12)
    plt.ylabel('Rata-rata Tekanan Darah (mmHg)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    print("\nGrafik Tren Tekanan Darah telah ditampilkan!")

def grafik_gula_darah():
    df =load_data_pasients()
    gula_harian = df.groupby('tanggal_periksa')['gula_darah'].mean()
    
    plt.figure(figsize=(12, 6))
    plt.plot(gula_harian.index, gula_harian.values, marker='s', linewidth=2, markersize=8, color='green')
    plt.title('Grafik Tren Gula Darah', fontsize=16, fontweight='bold')
    plt.xlabel('Tanggal Pemeriksaan', fontsize=12)
    plt.ylabel('Rata-rata Gula Darah (mg/dL)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    print("\nGrafik Tren Gula Darah telah ditampilkan!")

def grafik_kolesterol():
    df =load_data_pasients()
    kolesterol_harian = df.groupby('tanggal_periksa')['kolesterol'].mean()
    
    plt.figure(figsize=(12, 6))
    plt.plot(kolesterol_harian.index, kolesterol_harian.values, marker='^', linewidth=2, markersize=8, color='blue')
    plt.title('Grafik Tren Kolesterol', fontsize=16, fontweight='bold')
    plt.xlabel('Tanggal Pemeriksaan', fontsize=12)
    plt.ylabel('Rata-rata Kolesterol (mg/dL)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    print("\nGrafik Tren Kolesterol telah ditampilkan!")

def grafik_perbandingan():
    df =load_data_pasients()
    
    tekanan_harian = df.groupby('tanggal_periksa')['tekanan_darah'].mean()
    gula_harian = df.groupby('tanggal_periksa')['gula_darah'].mean()
    kolesterol_harian = df.groupby('tanggal_periksa')['kolesterol'].mean()
    
    plt.figure(figsize=(15, 7))
    
    plt.subplot(3, 1, 1)
    plt.plot(tekanan_harian.index, tekanan_harian.values, marker='o', linewidth=2, markersize=6, color='red')
    plt.title('Grafik Tren Tekanan Darah', fontsize=14, fontweight='bold')
    plt.ylabel('Tekanan Darah (mmHg)', fontsize=11)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    plt.subplot(3, 1, 2)
    plt.plot(gula_harian.index, gula_harian.values, marker='s', linewidth=2, markersize=6, color='green')
    plt.title('Grafik Tren Gula Darah', fontsize=14, fontweight='bold')
    plt.ylabel('Gula Darah (mg/dL)', fontsize=11)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    plt.subplot(3, 1, 3)
    plt.plot(kolesterol_harian.index, kolesterol_harian.values, marker='^', linewidth=2, markersize=6, color='blue')
    plt.title('Grafik Tren Kolesterol', fontsize=14, fontweight='bold')
    plt.xlabel('Tanggal Pemeriksaan', fontsize=11)
    plt.ylabel('Kolesterol (mg/dL)', fontsize=11)
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print("\nGrafik Perbandingan Semua Indikator telah ditampilkan!")

def kategori_risiko():
    df =load_data_pasients()
    
    df['kategori_tekanan'] = 'Normal'
    df.loc[df['tekanan_darah'] >= 120, 'kategori_tekanan'] = 'Perlu Waspada'
    df.loc[df['tekanan_darah'] > 140, 'kategori_tekanan'] = 'Risiko Tinggi'
    
    df['kategori_gula'] = 'Normal'
    df.loc[df['gula_darah'] >= 100, 'kategori_gula'] = 'Perlu Waspada'
    df.loc[df['gula_darah'] > 125, 'kategori_gula'] = 'Risiko Tinggi'
    
    df['kategori_kolesterol'] = 'Normal'
    df.loc[df['kolesterol'] >= 200, 'kategori_kolesterol'] = 'Perlu Waspada'
    df.loc[df['kolesterol'] > 240, 'kategori_kolesterol'] = 'Risiko Tinggi'
    
    df['kategori_akhir'] = 'Normal'
    
    kondisi_waspada = ((df['kategori_tekanan'] == 'Perlu Waspada') | 
                       (df['kategori_gula'] == 'Perlu Waspada') | 
                       (df['kategori_kolesterol'] == 'Perlu Waspada'))
    df.loc[kondisi_waspada, 'kategori_akhir'] = 'Perlu Waspada'
    
    kondisi_tinggi = ((df['kategori_tekanan'] == 'Risiko Tinggi') | 
                      (df['kategori_gula'] == 'Risiko Tinggi') | 
                      (df['kategori_kolesterol'] == 'Risiko Tinggi'))
    df.loc[kondisi_tinggi, 'kategori_akhir'] = 'Risiko Tinggi'
    
    kategori_count = df.groupby('kategori_akhir')['id_pasien'].count()
    
    plt.figure(figsize=(10, 8))
    colors = ['green', 'orange', 'red']
    explode = (0.1, 0, 0)
    
    plt.pie(kategori_count.values, labels=kategori_count.index, autopct='%1.1f%%', 
            startangle=90, colors=colors, explode=explode, shadow=True, textprops={'fontsize': 12})
    plt.title('Kategori Risiko Kesehatan Pasien', fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.show()
    
    print("\nKategori Risiko Kesehatan Pasien telah ditampilkan!")

def rata_rata_indikator():
    df =load_data_pasients()
    
    rata_tekanan = df['tekanan_darah'].mean()
    rata_gula = df['gula_darah'].mean()
    rata_kolesterol = df['kolesterol'].mean()
    
    indikator = ['Tekanan Darah', 'Gula Darah', 'Kolesterol']
    nilai = [rata_tekanan, rata_gula, rata_kolesterol]
    warna = ['red', 'green', 'blue']
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(indikator, nilai, color=warna, alpha=0.7, edgecolor='black', linewidth=1.5)
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:.2f}',
                 ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    plt.title('Rata-Rata Indikator Kesehatan Pasien', fontsize=16, fontweight='bold')
    plt.ylabel('Nilai Rata-Rata', fontsize=12)
    plt.xlabel('Indikator Kesehatan', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    print("\nRata-Rata Indikator Kesehatan Pasien telah ditampilkan!")

def risiko_tertinggi():
    df =load_data_pasients()
    
    pasien_stats = df.groupby('nama')[['tekanan_darah', 'gula_darah', 'kolesterol']].mean()
    top_pasien = pasien_stats.sort_values('tekanan_darah', ascending=False).head(5)
    
    plt.figure(figsize=(12, 6))
    x = range(len(top_pasien))
    width = 0.25
    
    plt.bar([i - width for i in x], top_pasien['tekanan_darah'], width=width, label='Tekanan Darah', color='red', alpha=0.7)
    plt.bar(x, top_pasien['gula_darah'], width=width, label='Gula Darah', color='green', alpha=0.7)
    plt.bar([i + width for i in x], top_pasien['kolesterol'], width=width, label='Kolesterol', color='blue', alpha=0.7)
    
    plt.xlabel('Nama Pasien', fontsize=12)
    plt.ylabel('Nilai Indikator', fontsize=12)
    plt.title('Pasien Risiko Tertinggi', fontsize=16, fontweight='bold')
    plt.xticks(x, top_pasien.index, rotation=45)
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()
    
    print("\nPasien Risiko Tertinggi telah ditampilkan!")

# Program Utama
if __name__ == "__main__":
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-10): ")
        
        match pilihan:
            case '1':
                ringkasan_data()
            case '2':
                analisis_kesehatan()
            case '3':
                grafik_tekanan_darah()
            case '4':
                grafik_gula_darah()
            case '5':
                grafik_kolesterol()
            case '6':
                grafik_perbandingan()
            case '7':
                kategori_risiko()
            case '8':
                rata_rata_indikator()
            case '9':
                risiko_tertinggi()
            case '10':
                print("Terima kasih telah menggunakan sistem ini. Sampai jumpa!")
        
        input("\nTekan Enter untuk melanjutkan...")