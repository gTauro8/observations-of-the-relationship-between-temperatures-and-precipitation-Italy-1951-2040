# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:27:46 2022

@author: giuse
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

df = pd.read_excel('temperature.xlsx', sheet_name= 'valori_a_10_anni')
print(df)

plt.rcParams["figure.figsize"] = (8, 4)        
#temperatura media
df.plot(x='Anni', y = 'temperatura_media', color = 'green')
plt.title('Media Temperatura in Italia dal 1901 al 2020')
plt.xlabel('Anni')
plt.ylabel('temperatura(C°)')
plt.savefig('media_temperature.png')
plt.show()

df.plot(x='Anni', y= 'V-VA_media', color = "red")
plt.title('Variazione Temperature medie in Italia dal 1901 al 2020')
plt.xlabel('Anni')
plt.ylabel('V-VA')
plt.savefig('variazioni_VA_temp_media.png')

#temperatura minima
df.plot(x='Anni', y = 'temperatura_min', color='purple')
plt.title('Temperatura minima in Italia dal 1901 al 2020')
plt.xlabel('Anni')
plt.ylabel('temperatura(C°)')
plt.savefig('temperature_minime.png')
plt.show()

df.plot(x='Anni', y= 'V-VA_min', color = "blue")
plt.title('Variazione temperature minime in Italia dal 1901 al 2020')
plt.xlabel('Anni')
plt.ylabel('V-VA')
plt.savefig('variazioni_VA_temp_minime.png')

#temperatura massima
df.plot(x='Anni', y = 'temperatura_max')
plt.title('Temperatura massime in Italia dal 1901 al 2020')
plt.xlabel('Anni')
plt.ylabel('temperatura(C°)')
plt.savefig('temperature_massime.png')
plt.show()

df.plot(x='Anni', y= 'V-VA_max', color = "yellow")
plt.title('Variazione temperatura massima in Italia dal 1901 al 2020')
plt.xlabel('Anni')
plt.ylabel('V-VA')
plt.savefig('variazioni_VA_temp_max.png')

#plot fill between
fig, ax = plt.subplots()
plt.title('Confronto temperature max, min e medie')
plt.xlabel('Anni')
plt.ylabel('Temperature')
ax.fill_between(df['Anni'], df['temperatura_max'], df['temperatura_min'], color='orange',alpha=.3 , linewidth=0)
ax.fill_between(df['Anni'], df['temperatura_min'], df['temperatura_media'],color='blue', alpha=.3 , linewidth=0)
ax.plot(df['Anni'], df['temperatura_max'], linewidth=3)
ax.plot(df['Anni'], df['temperatura_min'], linewidth=3)

ax2 = ax.twinx()
plt.ylim(4 , 20)
ax2.plot(df['Anni'], df['temperatura_media'], color = 'green', linewidth=3)

fig.legend(['temperatura minima(C°)', 'temperatura massima(C°)','Range tra max e med' ,'Range tra max e med' ,'temperatura media(C°)'], loc = 'upper right')


for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(20)
plt.savefig('confronto_temperature.png', dpi = 400)
plt.show()

#temperatura media
fig, ax = plt.subplots()
ax.bar(df['Anni'], df["temperatura_media"], color="C0", width=0.4)
plt.ylabel('Media temperature(C°)')
ax2 = ax.twinx()
ax2.plot(df["Anni"], df["V-%_media"], color="C1", marker="D", ms=5)

ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)

fig.set_figheight(8)
fig.set_figwidth(12)
plt.savefig('variazione_percentuale_temperature_medie.png', dpi = 400)
plt.show()

#temperatura max
fig, ax = plt.subplots()
ax.bar(df['Anni'], df["temperatura_max"], color="C2", width=0.4)
plt.ylabel('Media temperature(C°)')
ax2 = ax.twinx()
ax2.plot(df["Anni"], df["V-%_max"], color="C3", marker="D", ms=5)

ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis="y", colors="C2")
ax2.tick_params(axis="y", colors="C3")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)

fig.set_figheight(8)
fig.set_figwidth(12)
plt.savefig('variazione_percentuale_su_temperature_massime_medie.png', dpi = 400)
plt.show()

#temperatura min
fig, ax = plt.subplots()
ax.bar(df['Anni'], df["temperatura_min"], color="C4", width=0.4)
plt.ylabel('Media temperature(C°)')
ax2 = ax.twinx()
ax2.plot(df["Anni"], df["V-%_min"], color="C1", marker="D", ms=5)

ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis="y", colors="C4")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)

fig.set_figheight(8)
fig.set_figwidth(12)
plt.savefig('variazione_percentuale_su_media_temperature_minime.png', dpi = 400)
plt.show()



