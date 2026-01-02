import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data_pasien.csv')

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

print("Pasien Risiko Tertinggi telah ditampilkan!")
print("\nData Top 5 Pasien:")
print(top_pasien)