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
ax2.plot(df["Anni"], df2["rcp_26_50"], color="C1",marker="D", ms=5)

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura media scenario 2.6 percentile 50')
plt.savefig('1_precipitazionivstempmed26_50.png', dpi = 400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_85_50"], color="C1", width=0.4)
ax2 = ax.twinx()
ax2.plot(df2["Anni"], df2["rcp_85_50"], color="C4",marker="D", ms=5)

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura media scenario 8.5 percentile 50')
plt.savefig('2_precipitazionivstempmed85_50.png', dpi = 400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_26_10"], color="C9", width=0.4)
ax2 = ax.twinx()
ax2.plot(df2["Anni"], df2["rcp_26_10"], color="C10",marker="D", ms=5)

ax.tick_params(axis="y", colors="C9")
ax2.tick_params(axis="y", colors="C10")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura media scenario 2.6 percentile 10')
plt.savefig('3_precipitazionivstempmed26_10.png', dpi = 400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_85_10"], color="C4", width=0.4)
ax2 = ax.twinx()
ax2.plot(df2["Anni"], df2["rcp_85_10"], color="C6",marker="D", ms=5)

ax.tick_params(axis="y", colors="C4")
ax2.tick_params(axis="y", colors="C6")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura media scenario 8.5 percentile 10')
plt.savefig('4_precipitazionivstempmed85_10.png', dpi = 400)
plt.show()

fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_26_10"], color="C9", width=0.4)
ax2 = ax.twinx()
ax2.plot(df2["Anni"], df2["rcp_26_10"], color="C10",marker="D", ms=5)

ax.tick_params(axis="y", colors="C10")
ax2.tick_params(axis="y", colors="C11")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura media scenario 2.6 percentile 90')
plt.savefig('5_precipitazionivstempmed26_90.png', dpi = 400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_85_10"], color="C7", width=0.4)
ax2 = ax.twinx()
ax2.plot(df2["Anni"], df2["rcp_85_10"], color="C8",marker="D", ms=5)

ax.tick_params(axis="y", colors="C7")
ax2.tick_params(axis="y", colors="C8")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura media scenario 8.5 percentile 90')
plt.savefig('6_precipitazionivstempmed85_90.png', dpi = 400)
plt.show()

################################################################################################
#temperature max

fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_26_50"], color="C0", width=0.4)
ax2 = ax.twinx()
ax2.plot(df3["Anni"], df3["rcp_26_50"], color="C1",marker="D", ms=5)

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura massima scenario 2.6 percentile 50')
plt.savefig('7_precipitazionivstempmax26_50.png', dpi = 400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_85_50"], color="C1", width=0.4)
ax2 = ax.twinx()
ax2.plot(df3["Anni"], df3["rcp_85_50"], color="C4",marker="D", ms=5)

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura massima scenario 8.5 percentile 50')
plt.savefig('8_precipitazionivstempmax85_50.png', dpi = 400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_26_10"], color="C9", width=0.4)
ax2 = ax.twinx()
ax2.plot(df3["Anni"], df3["rcp_26_10"], color="C10",marker="D", ms=5)

ax.tick_params(axis="y", colors="C9")
ax2.tick_params(axis="y", colors="C10")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura massima scenario 2.6 percentile 10')
plt.savefig('9_precipitazionivstempmax26_10.png', dpi = 400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_85_10"], color="C4", width=0.4)
ax2 = ax.twinx()
ax2.plot(df3["Anni"], df3["rcp_85_10"], color="C6",marker="D", ms=5)

ax.tick_params(axis="y", colors="C4")
ax2.tick_params(axis="y", colors="C6")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura massima scenario 8.5 percentile 10')
plt.savefig('10_precipitazionivstempmax85_10.png', dpi = 400)
plt.show()

fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_26_10"], color="C9", width=0.4)
ax2 = ax.twinx()
ax2.plot(df3["Anni"], df3["rcp_26_10"], color="C10",marker="D", ms=5)

ax.tick_params(axis="y", colors="C10")
ax2.tick_params(axis="y", colors="C11")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura massima scenario 2.6 percentile 90')
plt.savefig('11_precipitazionivstempmax26_90.png', dpi = 400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_85_10"], color="C7", width=0.4)
ax2 = ax.twinx()
ax2.plot(df3["Anni"], df3["rcp_85_10"], color="C8",marker="D", ms=5)

ax.tick_params(axis="y", colors="C7")
ax2.tick_params(axis="y", colors="C8")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura massima scenario 8.5 percentile 90')
plt.savefig('12_precipitazionivstempmax85_90.png', dpi = 400)
plt.show()

################################################################################################
#temperature min

fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_26_50"], color="C0", width=0.4)
ax2 = ax.twinx()
ax2.plot(df4["Anni"], df4["rcp_26_50"], color="C1",marker="D", ms=5)

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura minima scenario 2.6 percentile 50')
plt.savefig('13_precipitazionivstempmin26_50.png', dpi = 400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_85_50"], color="C1", width=0.4)
ax2 = ax.twinx()
ax2.plot(df4["Anni"], df4["rcp_85_50"], color="C4",marker="D", ms=5)

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura minima scenario 8.5 percentile 50')
plt.savefig('14_precipitazionivstempmin85_50.png', dpi = 400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_26_10"], color="C9", width=0.4)
ax2 = ax.twinx()
ax2.plot(df4["Anni"], df4["rcp_26_10"], color="C10",marker="D", ms=5)

ax.tick_params(axis="y", colors="C9")
ax2.tick_params(axis="y", colors="C10")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura minima scenario 2.6 percentile 10')
plt.savefig('15_precipitazionivstempmin26_10.png', dpi = 400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_85_10"], color="C4", width=0.4)
ax2 = ax.twinx()
ax2.plot(df4["Anni"], df4["rcp_85_10"], color="C6",marker="D", ms=5)

ax.tick_params(axis="y", colors="C4")
ax2.tick_params(axis="y", colors="C6")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura minima scenario 8.5 percentile 10')
plt.savefig('16_precipitazionivstempmin85_10.png', dpi = 400)
plt.show()

fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_26_10"], color="C9", width=0.4)
ax2 = ax.twinx()
ax2.plot(df4["Anni"], df4["rcp_26_10"], color="C10",marker="D", ms=5)

ax.tick_params(axis="y", colors="C10")
ax2.tick_params(axis="y", colors="C11")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura minima scenario 2.6 percentile 90')
plt.savefig('17_precipitazionivstempmin26_90.png', dpi = 400)
plt.show()


fig, ax = plt.subplots()
ax.bar(df['Anni'], df["rcp_85_10"], color="C7", width=0.4)
ax2 = ax.twinx()
ax2.plot(df4["Anni"], df4["rcp_85_10"], color="C8",marker="D", ms=5)

ax.tick_params(axis="y", colors="C7")
ax2.tick_params(axis="y", colors="C8")

for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
fig.set_figheight(8)
fig.set_figwidth(12)
plt.title('Osservazione precipitazioni e temperatura minima scenario 8.5 percentile 90')
plt.savefig('18_precipitazionivstempmin85_90.png', dpi = 400)
plt.show()