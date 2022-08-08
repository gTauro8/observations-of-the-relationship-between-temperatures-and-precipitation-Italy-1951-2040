# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 19:20:49 2022

@author: giuse
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

df = pd.read_excel('confronti.xlsx')
print(df)

N = 12
area = (40 * np.random.rand(N))**2
colors = np.random.rand(N)

#temperatura media vs media precipitazioni

fig, ax = plt.subplots()
ax.bar(df['Anni'], df["media_precipitazioni"], color="C0", width=0.4)
plt.ylabel('Media precipitazioni(mm)')
ax2 = ax.twinx()
ax2.plot(df["Anni"], df["temperatura_media"], color="C1",marker="D", ms=5, label='temperatura media')

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)

plt.title('Rapporto tra Precipitazioni e Temperatura media dal 1901 al 2020')
fig.set_figheight(8)
fig.set_figwidth(12)
plt.legend()
plt.savefig('confronto_Temp_media_precipitazioni_medie.png', dpi = 400)
plt.show()


#temperatura massima vs media precipitazioni

fig, ax = plt.subplots()
ax.bar(df['Anni'], df["media_precipitazioni"], color="C3", width=0.4)
plt.ylabel('Media precipitazioni(mm)')
ax2 = ax.twinx()
ax2.plot(df["Anni"], df["temperatura_max"], color="C10",marker="D", ms=5, label='temperatura max')

ax.tick_params(axis="y", colors="C3")
ax2.tick_params(axis="y", colors="C10")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
plt.title('Rapporto tra Precipitazioni e Temperatura massima dal 1901 al 2020')
fig.set_figheight(8)
fig.set_figwidth(12)
plt.legend()
plt.savefig('confronto_Temp_max_precipitazioni_medie.png', dpi = 400)
plt.show()


#temperatura minima vs media precipitazioni

fig, ax = plt.subplots()
ax.bar(df['Anni'], df["media_precipitazioni"], color="C1", width=0.4)
plt.ylabel('Media precipitazioni(mm)')
ax2 = ax.twinx()
ax2.plot(df["Anni"], df["temperatura_min"], color="C2",marker="D", ms=5, label='temperatura min')

ax.tick_params(axis="y", colors="C1")
ax2.tick_params(axis="y", colors="C2")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)

plt.title('Rapporto tra Precipitazioni e Temperatura minima dal 1901 al 2020')
fig.set_figheight(8)
fig.set_figwidth(12)
plt.legend()
plt.savefig('confronto_Temp_min_precipitazioni_medie.png', dpi = 400)
plt.show()


plt.rcParams["figure.figsize"] = (8, 8) 
plt.scatter(df['V-VA_media'], df['V-VA'], s=area, c='green', alpha=0.3, label='V-VA precipitazioni e temperature medie')
plt.scatter(df['V-VA_max'], df['V-VA'],s=area, c='red', alpha=0.3, label='V-VA precipitazioni e temperature max')
plt.scatter(df['V-VA_min'], df['V-VA'],s=area, c='blue', alpha=0.3, label='V-VA precipitazioni e temperature min')
plt.xlabel('Variazioni temperature')
plt.ylabel('Variaizioni precipitazioni')
plt.title('Distribuzione tra variazione delle temperature e variazione delle precipitazioni')
plt.legend()
plt.savefig('1_distribuzione2.6.png', dpi=400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["media_precipitazioni"], color="skyblue", width=0.4)
plt.ylabel('Media precipitazioni(mm)')
ax2 = ax.twinx()
ax2.plot(df["Anni"], df["temperatura_min"], color="C1",marker="o", ms=5, label='temperatura min')
ax2.plot(df["Anni"], df["temperatura_max"], color="C2",marker="o", ms=5,label='temperatura mmax')
ax2.plot(df["Anni"], df["temperatura_media"], color="C3",marker="o", ms=5, label='temperatura media')
plt.title('Rapporto tra Precipitazioni e Temperatura dal 1901 al 2020')

ax.tick_params(axis="y", colors="C1")
ax2.tick_params(axis="y", colors="C2")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)

fig.set_figheight(8)
fig.set_figwidth(12)
plt.legend()
plt.savefig('confronto_Temp__precipitazioni.png', dpi = 600)
plt.show()