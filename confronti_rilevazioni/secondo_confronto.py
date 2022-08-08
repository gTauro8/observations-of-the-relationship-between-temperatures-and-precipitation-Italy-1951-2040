# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 18:55:09 2022

@author: giuse
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

df = pd.read_excel('mainconfronti.xlsx',  sheet_name='precipitazioni')
print(df)

df2 = pd.read_excel('mainconfronti.xlsx',  sheet_name='temperatura_media')
print(df2)

df3 = pd.read_excel('mainconfronti.xlsx',  sheet_name='temperature_max')
print(df3)

df4 = pd.read_excel('mainconfronti.xlsx',  sheet_name='temperatura_min')
print(df4)

#temperature medie

fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_26_50"], color="C0", width=0.4)
ax2 = ax.twinx()
ax2.plot(df["Anni"], df2["rcp_26_50"], color="C1",marker="o", ms=7, label = 'temperatura media')
ax2.plot(df["Anni"], df3["rcp_26_50"], color="C3",marker="o", ms=7, label = 'temperatura max')
ax2.plot(df["Anni"], df4["rcp_26_50"], color="C6",marker="o", ms=7, label = 'temperatura min')

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.legend()
plt.title('Confronto precipitazioni e temperatura media scenario 2.6 percentile 50')
plt.savefig('scenario26_50.png', dpi = 400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_85_50"], color="C0", width=0.4)
ax2 = ax.twinx()
ax2.plot(df["Anni"], df2["rcp_85_50"], color="C1",marker="o", ms=7, label = 'temperatura media')
ax2.plot(df["Anni"], df3["rcp_85_50"], color="C3",marker="o", ms=7, label = 'temperatura max')
ax2.plot(df["Anni"], df4["rcp_85_50"], color="C6",marker="o", ms=7, label = 'temperatura min')

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.legend()
plt.title('Confronto precipitazioni e temperatura media scenario 8.5 percentile 50')
plt.savefig('scenario85_50.png', dpi = 400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_26_10"], color="C0", width=0.4)
ax2 = ax.twinx()
ax2.plot(df["Anni"], df2["rcp_26_10"], color="C1",marker="o", ms=7, label = 'temperatura media')
ax2.plot(df["Anni"], df3["rcp_26_10"], color="C3",marker="o", ms=7, label = 'temperatura max')
ax2.plot(df["Anni"], df4["rcp_26_10"], color="C6",marker="o", ms=7, label = 'temperatura min')

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.legend()
plt.title('Confronto precipitazioni e temperatura media scenario 2.6 percentile 10')
plt.savefig('scenario26_10.png', dpi = 400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_26_90"], color="C0", width=0.4)
ax2 = ax.twinx()
ax2.plot(df["Anni"], df2["rcp_26_90"], color="C1",marker="o", ms=7, label = 'temperatura media')
ax2.plot(df["Anni"], df3["rcp_26_90"], color="C3",marker="o", ms=7, label = 'temperatura max')
ax2.plot(df["Anni"], df4["rcp_26_90"], color="C6",marker="o", ms=7, label = 'temperatura min')

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
plt.legend()
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Confronto precipitazioni e temperatura media scenario 2.6 percentile 90')
plt.savefig('scenario26_90.png', dpi = 400)
plt.show()

fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_85_10"], color="C0", width=0.4)
ax2 = ax.twinx()
ax2.plot(df["Anni"], df2["rcp_85_10"], color="C1",marker="o", ms=7, label = 'temperatura media')
ax2.plot(df["Anni"], df3["rcp_85_10"], color="C3",marker="o", ms=7, label = 'temperatura max')
ax2.plot(df["Anni"], df4["rcp_85_10"], color="C6",marker="o", ms=7, label = 'temperatura min')

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.legend()
plt.title('Confronto precipitazioni e temperatura media scenario 8.5 percentile 10')
plt.savefig('scenario85_10.png', dpi = 400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_85_90"], color="C0", width=0.4)
ax2 = ax.twinx()
ax2.plot(df["Anni"], df2["rcp_85_90"], color="C1",marker="o", ms=7, label = 'temperatura media')
ax2.plot(df["Anni"], df3["rcp_85_90"], color="C3",marker="o", ms=7, label = 'temperatura max')
ax2.plot(df["Anni"], df4["rcp_85_90"], color="C6",marker="o", ms=7, label = 'temperatura min')

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.legend()
plt.title('Confronto precipitazioni e temperatura media scenario 8.5 percentile 90')
plt.savefig('scenario85_90.png', dpi = 400)
plt.show()