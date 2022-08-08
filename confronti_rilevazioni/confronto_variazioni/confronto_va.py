import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

df = pd.read_excel('mainconfronti.xlsx',  sheet_name='VA_prec')
print(df)

df2 = pd.read_excel('mainconfronti.xlsx',  sheet_name='VA_max')
print(df2)

df3 = pd.read_excel('mainconfronti.xlsx',  sheet_name='VA_min')
print(df3)

df4 = pd.read_excel('mainconfronti.xlsx',  sheet_name='VA_media')
print(df4)

N = 7
area = (40 * np.random.rand(7))**2
colors = np.random.rand(7)


#plt.plot(df2['Anni'], df2['rcp_26_90'], color = "blue", linestyle='-.', label='Scenario 2.6 percentile 90%')
#plt.plot(df2['Anni'], df2['rcp_26_10'], color = "red", linestyle='dotted', label='Scenario 2.6 percentile 10%' )
#plt.plot(df2['Anni'], df2['rcp_26_50'], color = "green", linestyle='--', label='Scenario 2.6 percentile 50%' )

#plt.plot(df2['Anni'], df2['rcp_85_90'], color = "green", linestyle='-.', label='Scenario 8.5 percentile 90%')
#plt.plot(df2['Anni'], df2['rcp_85_10'], color = "blue", linestyle='dotted', label='Scenario 8.5 percentile 10%' )
#plt.plot(df2['Anni'], df2['rcp_85_50'], color = "red", linestyle='--', label='Scenario 8.5 percentile 50%' )

#confronto VA precipitazioni vs VA Temp Medie
plt.rcParams["figure.figsize"] = (8, 5) 
plt.scatter(df['VA_26_90'], df2['VA_26_90'], s=area, c='blue', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p90' )
plt.scatter(df['VA_26_50'], df2['VA_26_50'], s=area, c='pink', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p50' )
plt.scatter(df['VA_26_10'], df2['VA_26_10'], s=area, c='green', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p10' )

plt.title('Distribuzione tra variazioni delle precipitazioni e variazioni delle temperature massime')

plt.legend()
plt.savefig('1_distribuzione2.6.png', dpi = 600)
plt.show()


plt.rcParams["figure.figsize"] = (8, 5) 
plt.scatter(df['VA_85_90'], df2['VA_85_90'], s=area, c='blue', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p90' )
plt.scatter(df['VA_85_50'], df2['VA_85_50'], s=area, c='pink', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p50' )
plt.scatter(df['VA_85_10'], df2['VA_85_10'], s=area, c='green', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p10' )

plt.title('Distribuzione tra variazioni delle precipitazioni e variazioni delle temperature massime')
plt.legend()
plt.savefig('2_distribuzione8.5.png', dpi = 600)
plt.show()


plt.rcParams["figure.figsize"] = (8, 5) 
plt.scatter(df['VA_26_90'], df3['VA_26_90'], s=area, c='blue', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p90' )
plt.scatter(df['VA_26_50'], df3['VA_26_50'], s=area, c='pink', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p50' )
plt.scatter(df['VA_26_10'], df3['VA_26_10'], s=area, c='green', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p10' )

plt.title('Distribuzione tra variazioni delle precipitazioni e variazioni delle temperature minime')

plt.legend()
plt.savefig('1_1_distribuzione2.6.png', dpi = 600)
plt.show()


plt.rcParams["figure.figsize"] = (8, 5) 
plt.scatter(df['VA_85_90'], df3['VA_85_90'], s=area, c='blue', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p90' )
plt.scatter(df['VA_85_50'], df3['VA_85_50'], s=area, c='pink', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p50' )
plt.scatter(df['VA_85_10'], df3['VA_85_10'], s=area, c='green', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p10' )

plt.title('Distribuzione tra variazioni delle precipitazioni e variazioni delle temperature minime')
plt.legend()
plt.savefig('2_1_distribuzione8.5.png', dpi = 600)
plt.show()


plt.rcParams["figure.figsize"] = (8, 5) 
plt.scatter(df['VA_26_90'], df4['VA_26_90'], s=area, c='blue', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p90' )
plt.scatter(df['VA_26_50'], df4['VA_26_50'], s=area, c='pink', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p50' )
plt.scatter(df['VA_26_10'], df4['VA_26_10'], s=area, c='green', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p10' )

plt.title('Distribuzione tra variazioni delle precipitazioni e variazioni delle temperature medie')

plt.legend()
plt.savefig('1_2_distribuzione2.6.png', dpi = 600)
plt.show()


plt.rcParams["figure.figsize"] = (8, 5) 
plt.scatter(df['VA_85_90'], df4['VA_85_90'], s=area, c='blue', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p90' )
plt.scatter(df['VA_85_50'], df4['VA_85_50'], s=area, c='pink', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p50' )
plt.scatter(df['VA_85_10'], df4['VA_85_10'], s=area, c='green', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p10' )

plt.title('Distribuzione tra variazioni delle precipitazioni e variazioni delle temperature medie')
plt.legend()
plt.savefig('2_2_distribuzione8.5.png', dpi = 600)
plt.show()


################################################
plt.rcParams["figure.figsize"] = (8, 5) 
plt.scatter(df['VA_26_90'], df3['VA_26_90'], s=area, c='blue', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p90' )
plt.scatter(df['VA_85_90'], df3['VA_85_90'], s=area, c='pink', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p90' )
plt.title('Confronto distribuzioni degli scenari 2.6 e 8.6 con p90 per precipitazioni e temperature minime')
plt.legend()
plt.savefig('3_2distribuzione2.6vs8.5p90.png', dpi = 600)
plt.show()

plt.rcParams["figure.figsize"] = (8, 5) 
plt.scatter(df['VA_26_50'], df3['VA_26_50'], s=area, c='green', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p50' )
plt.scatter(df['VA_85_50'], df3['VA_85_50'], s=area, c='red', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p50' )
plt.title('Confronto distribuzioni degli scenari 2.6 e 8.6 con p90 per precipitazioni e temperature minime')
plt.legend()
plt.savefig('4_2distribuzione2.6vs8.5p50.png', dpi = 600)
plt.show()

plt.rcParams["figure.figsize"] = (8, 5) 
plt.scatter(df['VA_26_10'], df3['VA_26_10'], s=area, c='purple', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p10' )
plt.scatter(df['VA_85_10'], df3['VA_85_10'], s=area, c='yellow', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p10' )
plt.title('Confronto distribuzioni degli scenari 2.6 e 8.6 con p90 per precipitazioni e temperature minime')
plt.legend()
plt.savefig('5_2distribuzione2.6vs8.5p10.png', dpi = 600)
plt.show()

######################################################

plt.rcParams["figure.figsize"] = (8, 5) 
plt.scatter(df['VA_26_90'], df2['VA_26_90'], s=area, c='blue', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p90' )
plt.scatter(df['VA_85_90'], df2['VA_85_90'], s=area, c='pink', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p90' )

plt.title('Confronto distribuzioni degli scenari 2.6 e 8.6 con p90 per precipitazioni e temperature massime')
plt.legend()
plt.savefig('3_distribuzione2.6vs8.5p90.png', dpi = 600)
plt.show()

plt.rcParams["figure.figsize"] = (8, 5) 
plt.scatter(df['VA_26_50'], df2['VA_26_50'], s=area, c='green', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p50' )
plt.scatter(df['VA_85_50'], df2['VA_85_50'], s=area, c='red', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p50' )
plt.title('Confronto distribuzioni degli scenari 2.6 e 8.6 con p50 per precipitazioni e temperature massime')
plt.legend()
plt.savefig('4_distribuzione2.6vs8.5p50.png', dpi = 600)
plt.show()

plt.rcParams["figure.figsize"] = (8, 5) 
plt.scatter(df['VA_26_10'], df2['VA_26_10'], s=area, c='purple', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p10' )
plt.scatter(df['VA_85_10'], df2['VA_85_10'], s=area, c='yellow', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p10' )
plt.title('Confronto distribuzioni degli scenari 2.6 e 8.6 con p10 per precipitazioni e temperature massime')
plt.legend()
plt.savefig('5_distribuzione2.6vs8.5p10.png', dpi = 600)
plt.show()

####################################################
plt.rcParams["figure.figsize"] = (8, 5) 
plt.scatter(df['VA_26_90'], df4['VA_26_90'], s=area, c='blue', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p90' )
plt.scatter(df['VA_85_90'], df4['VA_85_90'], s=area, c='pink', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p90' )
plt.title('Confronto distribuzioni degli scenari 2.6 e 8.6 con p90 per precipitazioni e temperature medie')
plt.legend()
plt.savefig('3_1distribuzione2.6vs8.5p90.png', dpi = 600)
plt.show()

plt.rcParams["figure.figsize"] = (8, 5) 
plt.scatter(df['VA_26_50'], df4['VA_26_50'], s=area, c='green', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p50' )
plt.scatter(df['VA_85_50'], df4['VA_85_50'], s=area, c='red', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p50' )
plt.title('Confronto distribuzioni degli scenari 2.6 e 8.6 con p90 per precipitazioni e temperature medie')
plt.legend()
plt.savefig('4_1distribuzione2.6vs8.5p50.png', dpi = 600)
plt.show()

plt.rcParams["figure.figsize"] = (8, 5) 
plt.scatter(df['VA_26_10'], df4['VA_26_10'], s=area, c='purple', alpha=0.5, label='Distribuzione delle variazioni scenario 2.6 p10' )
plt.scatter(df['VA_85_10'], df4['VA_85_10'], s=area, c='yellow', alpha=0.5, label='Distribuzione delle variazioni scenario 8.5 p10' )
plt.title('Confronto distribuzioni degli scenari 2.6 e 8.6 con p90 per precipitazioni e temperature medie')
plt.legend()
plt.savefig('5_1distribuzione2.6vs8.5p10.png', dpi = 600)
plt.show()