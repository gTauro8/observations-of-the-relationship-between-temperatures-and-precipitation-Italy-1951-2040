# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:27:46 2022

@author: giuse
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

df = pd.read_excel('temperatura_italia.xlsx', sheet_name= 'temperature_a_20_anni')
print(df)

#plot
fig, ax = plt.subplots()

ax.fill_between(df['anni'], df['temperatura_min_media'], df['temperatura_max_media'], alpha=.3 , linewidth=0)
ax.plot(df['anni'], df['temperatura_min_media'], df['temperatura_max_media'], linewidth=2)

ax2 = ax.twinx()
plt.ylim(4 , 20)
ax2.plot(df['anni'], df['temperatura_media'], color = 'green')


plt.grid(True)
fig.legend(['temperatura minima(C°)', 'temperatura massima(C°)','Range tra max e min' ,'temperatura media(C°)'], loc = 'upper right')


for tick in ax.get_xticklabels():
        tick.set_rotation(25)
        
plt.show()