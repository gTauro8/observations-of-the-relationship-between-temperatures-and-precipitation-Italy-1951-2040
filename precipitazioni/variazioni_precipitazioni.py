# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


df = pd.read_excel('precipitazioni_italia.xlsx', sheet_name= 'valori_a_20_anni')
print(df)

df.plot(x='anni', y = 'media_precipitazioni')
plt.title('Media Precipitazioni in Italia dal 1901 al 2020')
plt.xlabel('Anni')
plt.ylabel('Media precipitazioni(mm)')
plt.savefig('media_precipitazioni.png', dpi = 400)
plt.show()

df.plot(x='anni', y= 'V-VA', color = "red")
plt.title('Variazione Precipitazioni in Italia dal 1901 al 2020')
plt.xlabel('Anni')
plt.ylabel('V-VA')
plt.savefig('variazioni_VA_precipitazioni.png', dpi = 400)


fig, ax = plt.subplots()
ax.bar(df['anni'], df["media_precipitazioni"], color="C0")
plt.ylabel('Media precipitazioni(mm)')
ax2 = ax.twinx()
ax2.plot(df["anni"], df["V-%"], color="C1", marker="D", ms=5)

ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
plt.savefig('variazione_percentuale_su_media_precipitazione.png', dpi = 400)
plt.show()
