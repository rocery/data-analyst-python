import pandas as pd
import datetime
import matplotlib.pyplot as plt

dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')

# Membuah kolom baru order_month yang diambil dari order_date dengan format YYYY-mm
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))
# Membuah kolom baru gmv hasil kali item_price dan quantity
dataset['gmv'] = dataset['item_price']*dataset['quantity']
# Membuat kolom baru new_column item_price dikali 2
dataset['new_column'] = dataset['item_price'].apply(lambda x: x*2)
# Membuat groupby berdasarkan order_month yang berisi total gmv
monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index()
# Menampilkan grafik monthly_amount
# plt.plot(monthly_amount['order_month'], monthly_amount['gmv'])

# Alternatif menampilkan grafik monthly_amount
# Mengubah ukuran figure menjadi panjang 15 inc tinggi 5 inch
fig = plt.figure(figsize=(15, 5))
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='o', linestyle='-.', linewidth=2)
# Menambah title pada grafik
plt.title('Monthly GMV Year 2019', loc='center', pad=20, fontsize=20, color='blue')
# Menambah Label X
plt.xlabel('Order Month', fontsize=15)
# Menambah Label Y
plt.ylabel('Total GMV/Amount (in Billions)', fontsize=15)
# Menambah grid
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
# Kostumisasi nilai awal sumbu Y
plt.ylim(ymin=0)
# Kostumisasi Y ticks (value Y)
labels, locations = plt.yticks() #List ticks labels di sumbu-y
plt.yticks(labels, (labels/1000000000).astype(int))
# Menambah text pada grafik
plt.text(0.45, 0.72, 'The GMV increased significantly on October 2019', transform=fig.transFigure, color='red')
# Menyimpan figure/grafik
plt.savefig('monthly_gmv.png', quality=95)
# Melihat format savefig yang didukung
# plt.gcf().canvas.get_supported_filetypes()
plt.show()
