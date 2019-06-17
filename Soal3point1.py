import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data
df1 = pd.read_csv('EXCLJK.csv', parse_dates=['Date'])
df1 = df1.set_index('Date')
df2 = pd.read_csv('FRENJK.csv', parse_dates=['Date'])
df2 = df2.set_index('Date')
df3 = pd.read_csv('ISATJK.csv', parse_dates=['Date'])
df3 = df3.set_index('Date')
df4 = pd.read_csv('TLKMJK.csv', parse_dates=['Date'])
df4 = df4.set_index('Date')

# print(df1.head(2))
# print(df2.head(2))
# print(df3.head(2))
# print(df4.head(2))

plt.style.use('ggplot')

plt.plot(
    df1.index, df1['Close'], 'g-',
    df2.index, df2['Close'], 'c-',
    df3.index, df3['Close'], 'b-',
    df4.index, df4['Close'], 'r-',
)

plt.title('Harga Historis Saham Provider Telco Indonesia')
plt.xlabel('Tanggal')
plt.ylabel('Rupiah(IDR)')
plt.xticks(rotation=65)
plt.grid(True)
plt.legend(['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk', 'PT. Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk'], loc=1)
plt.subplots_adjust(
    left=0.13, bottom=0.23, right=0.91, top=0.92,
    wspace=.2, hspace=.2
)

plt.show()