import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy import stats
from pandas.plotting import scatter_matrix
raw_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dataset_statistic.csv", sep=';')

# mengambil hanya data untuk produk 'A'
produk_A = raw_data[raw_data['Produk'] == 'A']
 
# menghitung rerata pendapatan menggunakan method .mean pada objek pandas DataFrame
print (produk_A['Pendapatan'].mean())
 
# menghitung rerata pendapatan menggunakan method .mean pada objek pandas DataFrame dengan numpy
print (np.mean(produk_A['Pendapatan']))

print (raw_data)
# Hitung median dari pendapatan menggunakan pandas
print (produk_A['Pendapatan'].median())
 
# Hitung median dari pendapatan menggunakan numpy
print (np.median(produk_A['Pendapatan']))

# Melihat jumlah dari masing-masing produk
print (raw_data['Produk'].value_counts())

# mencari median atau 50% dari data menggunakan pandas
print(raw_data['Pendapatan'].quantile(q = 0.5))
 
# mencari median atau 50% dari data menggunakan pandas
print(np.quantile(raw_data['Pendapatan'], q=0.5))

# menghitung rerata dan median 'Pendapatan' dan 'Harga'
print(raw_data[['Pendapatan', 'Harga']].agg([np.mean, np.median]))
 
# menghitung rerata dan median Pendapatan dan Harga dari tiap produk
print(raw_data[['Pendapatan', 'Harga', 'Produk']].groupby('Produk').agg([np.mean, np.median]))

# cari proporsi tiap Produk
print(raw_data['Produk'].value_counts()/raw_data.shape[0])

# Cari nilai rentang dari kolom 'Pendapatan'
print (raw_data['Pendapatan'].max() - raw_data['Pendapatan'].min())

# menghitung variansi umur menggunakan method .var() dari pandas
print (raw_data['Pendapatan'].var())
 
# menghitung variansi umur menggunakan method .var() dari numpy
print (np.var(raw_data['Pendapatan']))

# mengatur variansi populasi dengan method `.var()` dari pandas
print (raw_data['Pendapatan'].var(ddof=0))

# menghitung deviasi baku sampel pendapatan menggunakan method std() dari pandas
print (raw_data['Pendapatan'].std())
 
# menghitung deviasi baku sampel pendapatan menggunakan method std() dari numpy
print (np.std(raw_data['Pendapatan'], ddof = 1))

# menghitung korelasi dari setiap pasang variabel pada raw_data
print (raw_data.corr())

# mencari korelasi 'kendall' untuk tiap pasang variabel
print (raw_data.corr(method='kendall'))
 
# mencari korelasi 'spearman' untuk tiap pasang variabel
print (raw_data.corr(method='spearman'))

# ------------------------Visualisasi-------------------------
# Scatter
plt.figure()
# visualisasi diagram pencar untuk variabel 'Pendapatan' dan 'Total' menggunakan 'plot.scatter' dari pandas
raw_data.plot.scatter(x='Pendapatan', y='Total')
plt.title('plot.scatter dari pandas', size=14)
plt.tight_layout()
plt.show()

# visualisasi diagram pencar untuk variabel 'Pendapatan' dan 'Total' menggunakan 'plt.scatter' dari matplotlib
plt.scatter(x='Pendapatan', y='Total', data=raw_data)
plt.title('plt.scatter dari matplotlib', size=14)
plt.tight_layout()
plt.show()

# Histogram
plt.figure()
# melihat distribusi data kolom 'Pendapatan' menggunakan 'hist' dari pandas
raw_data.hist(column='Pendapatan')
plt.title('.hist dari pandas', size=14)
plt.tight_layout()
plt.show()

plt.figure()
# melihat distribusi data kolom 'Pendapatan' menggunakan 'pyplot.hist' dari matplotlib.pyplot
plt.hist(x='Pendapatan', data=raw_data)
plt.xlabel('Pendapatan')
plt.title('pyplot.hist dari matplotlib.pyplot', size=14)
plt.tight_layout()
plt.show()

# Boxplot
# melihat box plot dari kolom 'Pendapatan' menggunakan method '.boxplot' dari pandas
plt.figure()
raw_data.boxplot(column='Pendapatan')
plt.title('.boxplot dari pandas', size=14)
plt.tight_layout()
plt.show()

# melihat box plot dari kolom 'Pendapatan' menggunakan method '.boxplot' dari matplotlib
plt.figure()
plt.boxplot(x = 'Pendapatan', data=raw_data)
plt.xlabel('Pendapatan')
plt.title('pyplot.boxplot dari matplotlib.pyplot', size=14)
plt.tight_layout()
plt.show()

# Bar plot
# hitung frekuensi dari masing-masing nilai pada kolom 'Produk'
class_freq = raw_data['Produk'].value_counts()

# lihat nilai dari class_freq
print(class_freq)

plt.figure()
# membuat bar plot dengan method `plot.bar()` dari pandas
class_freq.plot.bar()
plt.title('.bar dari pandas', size=14)
plt.tight_layout()
plt.show()

plt.figure()
# membuat bar plot dengan method `plt.bar()` dari matplotlib
plt.bar(x=class_freq.index, height=class_freq.values)
plt.title('plt.bar dari matplotlib.pyplot', size=14)
plt.tight_layout()
plt.show()

# Pie chart
plt.figure()
# membuat pie chart menggunakan method 'pyplot.pie()' dari matplotlib
plt.pie(class_freq.values, labels=class_freq.index)
plt.title('plt.pie dari matplotlib.pyplot', size=14)
plt.tight_layout()
plt.show()

plt.figure()
# membuat pie chart menggunakan method 'plot.pie' dari pandas
class_freq.plot.pie()
plt.title('plot.pie dari pandas', size=14)
plt.tight_layout()
plt.show()

# Matriks Korelasi / hearmap / matshow
# mengatur ukuran gambar/plot
plt.rcParams['figure.dpi'] = 100

plt.figure()
plt.matshow(raw_data.corr())
plt.title('Plot correlation matriks dengan .matshow', size=14)
plt.tight_layout()
plt.show()

plt.figure()
sns.heatmap(raw_data.corr(), annot=True)
plt.title('Plot correlation matriks dengan sns.heatmap', size=14)
plt.tight_layout()
plt.show()

# Boxplot
plt.figure()
# boxplot biasa tanpa pengelompokkan
raw_data.boxplot(rot=90)
plt.title('Boxplot tanpa pengelompokkan', size=14)
plt.tight_layout()
plt.show()

plt.figure()
# box plot dengan pengelompokkan dilakukan oleh kolom 'Produk'
raw_data.boxplot(by='Produk')
plt.tight_layout()
plt.show()

# Grouped Histogram
plt.figure()
raw_data[raw_data['Produk'] == 'B'].hist()
plt.tight_layout()
plt.show()

# Hexbin plot
plt.figure()
raw_data.plot.hexbin(x='Pendapatan', y='Total', gridsize=25, rot=90)
plt.tight_layout()
plt.show()

# Scatter Matrix Plot
_, ax = plt.subplots(1, 1, figsize=(10,10))
scatter_matrix(raw_data, ax=ax)
plt.show()
# Density plot
_, ax = plt.subplots(1, 1, figsize=(10,10))
scatter_matrix(raw_data, diagonal='kde', ax=ax)
plt.show()
# ------------------------Transformasi-------------------------
plt.figure()
raw_data.hist()
plt.title('Histogram seluruh kolom', size=14)
plt.tight_layout()
plt.show()

plt.figure()
raw_data['Pendapatan'].hist()
plt.title('Histogram pendapatan', size=14)
plt.tight_layout()
plt.show()

plt.figure()
# transformasi menggunakan akar lima
np.power(raw_data['Pendapatan'], 1/5).hist()
plt.title('Histogram pendapatan - ransformasi menggunakan akar lima', size=14)
plt.tight_layout()
plt.show()

# simpan hasil transformasi
pendapatan_akar_lima = np.power(raw_data['Pendapatan'], 1/5)

plt.figure()
# membuat qqplot pendapatan - transformasi menggunakan akar lima
stats.probplot(pendapatan_akar_lima, plot=plt)
plt.title('qqplot pendapatan - transformasi menggunakan akar lima', size=14)
plt.tight_layout()
plt.show()

plt.figure()
# membuat qqplot pendapatan
stats.probplot(raw_data['Pendapatan'], plot=plt)
plt.title('qqplot pendapatan', size=14)
plt.tight_layout()
plt.show()

# Transformasi Box-Cox
hasil, _ = stats.boxcox(raw_data['Pendapatan'])

plt.figure()
# Histogram
plt.hist(hasil)
plt.title('Histogram', size=14)
plt.tight_layout()
plt.show()

plt.figure()
# QQPlot
stats.probplot(hasil, plot=plt)
plt.title('qqplot', size=14)
plt.tight_layout()
plt.show()

# Transformasi Data Kategorik ke Dalam Angka
data_dummy_produk = pd.get_dummies(raw_data['Produk'])
print(data_dummy_produk)

# -------------------Regresi Linear Sedehana-----------------------
# variabel tak bebas
nilai_Y = raw_data[['Total']]

# variabel bebas
nilai_X = raw_data['Pendapatan']

# membuat model regresi linier
model_regresi = sm.OLS(endog = nilai_Y, exog=nilai_X).fit()

# melihat summary dari model
model_regresi.summary()