import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

# Scatterplot Produksi vs Penjualan untuk Dataset 1
plt.figure(figsize=(8, 6))
plt.scatter(df1['Produksi'], df1['Penjualan'], alpha=0.7, c='blue')
plt.title('Scatterplot Produksi vs Penjualan (Dataset 1)')
plt.xlabel('Produksi')
plt.ylabel('Penjualan')
plt.grid(True)
plt.show()

# Menghitung koefisien korelasi Pearson
correlation = df1['Produksi'].corr(df1['Penjualan'])
print(f"Koefisien Korelasi Pearson antara Produksi dan Penjualan (Dataset 1): {correlation}")

# Histogram Produksi dan Penjualan untuk Dataset 1
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(df1['Produksi'], bins=20, alpha=0.7, color='blue')
plt.title('Distribusi Produksi (Dataset 1)')
plt.xlabel('Produksi')
plt.ylabel('Frekuensi')

plt.subplot(1, 2, 2)
plt.hist(df1['Penjualan'], bins=20, alpha=0.7, color='orange')
plt.title('Distribusi Penjualan (Dataset 1)')
plt.xlabel('Penjualan')
plt.ylabel('Frekuensi')

plt.tight_layout()
plt.show()

# Statistik deskriptif
print("Statistik Deskriptif Produksi (Dataset 1):")
print(df1['Produksi'].describe())

print("\nStatistik Deskriptif Penjualan (Dataset 1):")
print(df1['Penjualan'].describe())

# Scatterplot Penjualan vs Persediaan untuk Dataset 2
plt.figure(figsize=(8, 6))
plt.scatter(df2['Penjualan'], df2['Persediaan'], alpha=0.7, c='green')
plt.title('Scatterplot Penjualan vs Persediaan (Dataset 2)')
plt.xlabel('Penjualan')
plt.ylabel('Persediaan')
plt.grid(True)
plt.show()

# Menghitung koefisien korelasi Pearson
correlation = df2['Penjualan'].corr(df2['Persediaan'])
print(f"Koefisien Korelasi Pearson antara Penjualan dan Persediaan (Dataset 2): {correlation}")

# Histogram Penjualan dan Persediaan untuk Dataset 2
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(df2['Penjualan'], bins=20, alpha=0.7, color='orange')
plt.title('Distribusi Penjualan (Dataset 2)')
plt.xlabel('Penjualan')
plt.ylabel('Frekuensi')

plt.subplot(1, 2, 2)
plt.hist(df2['Persediaan'], bins=20, alpha=0.7, color='green')
plt.title('Distribusi Persediaan (Dataset 2)')
plt.xlabel('Persediaan')
plt.ylabel('Frekuensi')

plt.tight_layout()
plt.show()

# Statistik deskriptif
print("Statistik Deskriptif Penjualan (Dataset 2):")
print(df2['Penjualan'].describe())

print("\nStatistik Deskriptif Persediaan (Dataset 2):")
print(df2['Persediaan'].describe())

# Scatterplot Produksi vs Persediaan untuk Dataset 3
plt.figure(figsize=(8, 6))
plt.scatter(df3['Produksi'], df3['Persediaan'], alpha=0.7, c='red')
plt.title('Scatterplot Produksi vs Persediaan (Dataset 3)')
plt.xlabel('Produksi')
plt.ylabel('Persediaan')
plt.grid(True)
plt.show()

# Menghitung koefisien korelasi Pearson
correlation = df3['Produksi'].corr(df3['Persediaan'])
print(f"Koefisien Korelasi Pearson antara Produksi dan Persediaan (Dataset 3): {correlation}")

# Histogram Produksi dan Persediaan untuk Dataset 3
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(df3['Produksi'], bins=20, alpha=0.7, color='blue')
plt.title('Distribusi Produksi (Dataset 3)')
plt.xlabel('Produksi')
plt.ylabel('Frekuensi')

plt.subplot(1, 2, 2)
plt.hist(df3['Persediaan'], bins=20, alpha=0.7, color='green')
plt.title('Distribusi Persediaan (Dataset 3)')
plt.xlabel('Persediaan')
plt.ylabel('Frekuensi')

plt.tight_layout()
plt.show()

# Statistik deskriptif
print("Statistik Deskriptif Produksi (Dataset 3):")
print(df3['Produksi'].describe())

print("\nStatistik Deskriptif Persediaan (Dataset 3):")
print(df3['Persediaan'].describe())
