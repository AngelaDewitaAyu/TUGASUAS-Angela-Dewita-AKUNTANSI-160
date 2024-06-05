import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Membuat data simulasi untuk beberapa dataset
np.random.seed(42)

# Dataset 1: Produksi dan Penjualan
data1 = {
    'Produksi': np.random.randint(50, 150, size=100),
    'Penjualan': np.random.randint(30, 130, size=100)
}

# Dataset 2: Penjualan dan Persediaan
data2 = {
    'Penjualan': np.random.randint(40, 140, size=100),
    'Persediaan': np.random.randint(20, 110, size=100)
}

# Dataset 3: Produksi dan Persediaan
data3 = {
    'Produksi': np.random.randint(70, 170, size=100),
    'Persediaan': np.random.randint(30, 120, size=100)
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

# Menampilkan beberapa baris pertama dari setiap dataset
print("Dataset 1:")
print(df1.head())

print("\nDataset 2:")
print(df2.head())

print("\nDataset 3:")
print(df3.head())

# Scatterplot untuk setiap dataset
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.scatter(df1['Produksi'], df1['Penjualan'], alpha=0.7, c='blue')
plt.title('Dataset 1: Produksi vs Penjualan')
plt.xlabel('Produksi')
plt.ylabel('Penjualan')
plt.grid(True)

plt.subplot(1, 3, 2)
plt.scatter(df2['Penjualan'], df2['Persediaan'], alpha=0.7, c='green')
plt.title('Dataset 2: Penjualan vs Persediaan')
plt.xlabel('Penjualan')
plt.ylabel('Persediaan')
plt.grid(True)

plt.subplot(1, 3, 3)
plt.scatter(df3['Produksi'], df3['Persediaan'], alpha=0.7, c='red')
plt.title('Dataset 3: Produksi vs Persediaan')
plt.xlabel('Produksi')
plt.ylabel('Persediaan')
plt.grid(True)

plt.tight_layout()
plt.show()

# Histogram untuk setiap dataset
plt.figure(figsize=(15, 10))

plt.subplot(3, 1, 1)
plt.hist(df1['Produksi'], bins=20, alpha=0.5, label='Produksi', color='blue')
plt.hist(df1['Penjualan'], bins=20, alpha=0.5, label='Penjualan', color='orange')
plt.title('Dataset 1: Histogram Produksi dan Penjualan')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.legend(loc='upper right')

plt.subplot(3, 1, 2)
plt.hist(df2['Penjualan'], bins=20, alpha=0.5, label='Penjualan', color='orange')
plt.hist(df2['Persediaan'], bins=20, alpha=0.5, label='Persediaan', color='green')
plt.title('Dataset 2: Histogram Penjualan dan Persediaan')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.legend(loc='upper right')

plt.subplot(3, 1, 3)
plt.hist(df3['Produksi'], bins=20, alpha=0.5, label='Produksi', color='blue')
plt.hist(df3['Persediaan'], bins=20, alpha=0.5, label='Persediaan', color='green')
plt.title('Dataset 3: Histogram Produksi dan Persediaan')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')
plt.legend(loc='upper right')

plt.tight_layout()
plt.show()

# Diagram Venn untuk setiap dataset
plt.figure(figsize=(15, 5))

# Mengonversi kolom menjadi set untuk diagram Venn
produksi_set1 = set(df1['Produksi'])
penjualan_set1 = set(df1['Penjualan'])

penjualan_set2 = set(df2['Penjualan'])
persediaan_set2 = set(df2['Persediaan'])

produksi_set3 = set(df3['Produksi'])
persediaan_set3 = set(df3['Persediaan'])

plt.subplot(1, 3, 1)
venn3([produksi_set1, penjualan_set1, set()], ('Produksi', 'Penjualan', ''))
plt.title('Dataset 1: Diagram Venn')

plt.subplot(1, 3, 2)
venn3([set(), penjualan_set2, persediaan_set2], ('', 'Penjualan', 'Persediaan'))
plt.title('Dataset 2: Diagram Venn')

plt.subplot(1, 3, 3)
venn3([produksi_set3, set(), persediaan_set3], ('Produksi', '', 'Persediaan'))
plt.title('Dataset 3: Diagram Venn')

plt.tight_layout()
plt.show()
