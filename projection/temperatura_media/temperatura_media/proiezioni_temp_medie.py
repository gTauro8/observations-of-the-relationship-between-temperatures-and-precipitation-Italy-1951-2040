# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 18:55:09 2022

@author: giuse
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

df = pd.read_excel('temperature_medie.xlsx',  sheet_name='valori_5_anni')
print(df)


plt.rcParams["figure.figsize"] = (8, 4) 
plt.plot(df['Anni'], df['rcp_26_90'], color = "blue", marker='o', label='Scenario 2.6 percentile 90%')
plt.plot(df['Anni'], df['rcp_26_10'], color = "red", marker='o', label='Scenario 2.6 percentile 10%' )
plt.plot(df['Anni'], df['rcp_26_50'], color = "green", marker='o', label='Scenario 2.6 percentile 50%' )
plt.title('Proiezioni Temperature Medie in Italia dal 2020 al 2039 Scenario 2.6')
plt.grid(True)
plt.xlabel('Anno')
plt.legend()
plt.savefig('1_ProiezioniTemperatureMedie2.6.png', dpi = 400)
plt.show()


plt.rcParams["figure.figsize"] = (8, 4) 
plt.plot(df['Anni'], df['rcp_85_90'], color = "green", marker='o', label='Scenario 8.5 percentile 90%')
plt.plot(df['Anni'], df['rcp_85_10'], color = "blue", marker='o', label='Scenario 8.5 percentile 10%' )
plt.plot(df['Anni'], df['rcp_85_50'], color = "red", marker='o', label='Scenario 8.5 percentile 50%' )
plt.title('Proiezioni Temperature Medie in Italia dal 2020 al 2039 Scenario 8.5')
plt.grid(True)
plt.xlabel('Anno')
plt.legend()
plt.savefig('2_ProiezioniTemperatureMedie8.5.png', dpi = 400)
plt.show()


plt.rcParams["figure.figsize"] = (8, 4) 
plt.plot(df['Anni'], df['rcp_26_90'], color = "green", label='Scenario 2.6 percentile 90%')
plt.plot(df['Anni'], df['rcp_26_10'], color = "blue", label='Scenario 2.6 percentile 10%' )
plt.plot(df['Anni'], df['rcp_26_50'], color = "red", label='Scenario 2.6 percentile 50%' )
plt.plot(df['Anni'], df['rcp_85_90'], color = "green", linestyle='--', label='Scenario 8.5 percentile 90%')
plt.plot(df['Anni'], df['rcp_85_10'], color = "blue", linestyle='--', label='Scenario 8.5 percentile 10%' )
plt.plot(df['Anni'], df['rcp_85_50'], color = "red", linestyle='--', label='Scenario 8.5 percentile 50%' )
plt.title('Proiezioni Temperature Medie in Italia dal 2020 al 2039 Scenari a confronto')
plt.grid(True)
plt.xlabel('Anno')
plt.legend()
plt.savefig('3_ProiezioniTemperatureMedie2020_2039scenariaconfronto.png', dpi = 400)
plt.show()


#situazione dal 2001 al 2039
df2 = pd.read_excel('temperature_medie.xlsx',  sheet_name='2001_2039')
print(df2)

plt.rcParams["figure.figsize"] = (8, 4) 
plt.plot(df2['Anni'], df2['rcp_26_90'], color = "blue", linestyle='-.', label='Scenario 2.6 percentile 90%')
plt.plot(df2['Anni'], df2['rcp_26_10'], color = "red", linestyle='dotted', label='Scenario 2.6 percentile 10%' )
plt.plot(df2['Anni'], df2['rcp_26_50'], color = "green", linestyle='--', label='Scenario 2.6 percentile 50%' )
plt.title('Confronto rilevazioni e proiezioni in Italia dal 2001 al 2039 Scenario 2.6')
plt.grid(True)
plt.xlabel('Anno')
plt.legend()
plt.savefig('4_ProiezioniTemperatureMedie2.62001_2039.png', dpi = 400)
plt.show()


plt.rcParams["figure.figsize"] = (8, 4) 
plt.plot(df2['Anni'], df2['rcp_85_90'], color = "green", linestyle='-.', label='Scenario 8.5 percentile 90%')
plt.plot(df2['Anni'], df2['rcp_85_10'], color = "blue", linestyle='dotted', label='Scenario 8.5 percentile 10%' )
plt.plot(df2['Anni'], df2['rcp_85_50'], color = "red", linestyle='--', label='Scenario 8.5 percentile 50%' )
plt.title('Confronto rilevazioni e proiezioni temperature medie in Italia dal 2001 al 2039 Scenario 8.5')
plt.grid(True)
plt.xlabel('Anno')
plt.legend()
plt.savefig('5_ProiezioniTemperatureMedie8.52001_2039.png', dpi = 400)
plt.show()

plt.rcParams["figure.figsize"] = (8, 4) 
plt.plot(df2['Anni'], df2['rcp_26_90'], color = "green", label='Scenario 2.6 percentile 90%')
plt.plot(df2['Anni'], df2['rcp_26_10'], color = "blue", label='Scenario 2.6 percentile 10%' )
plt.plot(df2['Anni'], df2['rcp_26_50'], color = "red", label='Scenario 2.6 percentile 50%' )
plt.plot(df2['Anni'], df2['rcp_85_90'], color = "green", linestyle='-.', label='Scenario 8.5 percentile 90%')
plt.plot(df2['Anni'], df2['rcp_85_10'], color = "blue", linestyle='-.', label='Scenario 8.5 percentile 10%' )
plt.plot(df2['Anni'], df2['rcp_85_50'], color = "red", linestyle='-.', label='Scenario 8.5 percentile 50%' )
plt.title('Confronto rilevazioni e proiezioni temperature medie in Italia dal 2001 al 2039 Scenari a confronto')
plt.grid(True)
plt.xlabel('Anno')
plt.legend()
plt.savefig('6_ProiezioniTemperatureMedie2001_2039scenariaconfronto.png', dpi = 400)
plt.show()
