# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter


df = pd.read_excel('precipitazioni.xlsx', sheet_name= 'valori_a_10_anni')
print(df)

plt.rcParams["figure.figsize"] = (8, 4)        
df.plot(x='Anni', y = 'media_precipitazioni')
plt.title('Media Precipitazioni in Italia dal 1901 al 2020')
plt.xlabel('Anni')
plt.ylabel('Media precipitazioni(mm)')
plt.savefig('media_precipitazioni.png')
plt.show()

df.plot(x='Anni', y= 'V-VA', color = "red")
plt.title('Variazione Precipitazioni in Italia dal 1901 al 2020')
plt.xlabel('Anni')
plt.ylabel('V-VA')
plt.savefig('variazioni_VA_precipitazioni.png')


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["media_precipitazioni"], color="C0", width=0.4)
plt.ylabel('Media precipitazioni(mm)')
ax2 = ax.twinx()
ax2.plot(df["Anni"], df["V-%"], color="C1",marker="D", ms=5)

ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Rapporto tra precipitazioni e variazioni % in Italia dal 1901 al 2020')
plt.savefig('variazione_percentuale_su_media_precipitazione.png', dpi = 400)
plt.show()
