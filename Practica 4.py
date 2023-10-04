import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os


#Dirección del archivo
archivo_csv = 'Practica 2\MineralesLimpios.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(archivo_csv)
df['date'] = pd.to_datetime(df['date'])


dfGold = df.loc[df['commodity'] == 'Gold', ['date', 'high']]
dfSilver = df.loc[df['commodity'] == 'Silver', ['date', 'high']]
dfCopper = df.loc[df['commodity'] == 'Copper', ['date', 'high']]
dfPlatinum = df.loc[df['commodity'] == 'Platinum', ['date', 'high']]
dfPalladium = df.loc[df['commodity'] == 'Palladium', ['date', 'high']]


#Distintos plots para los distintos metales :D

#plt.plot(dfGold['date'], dfGold['high'])
#plt.plot(dfSilver['date'], dfSilver['high'])
#plt.plot(dfCopper['date'], dfCopper['high'])
#plt.plot(dfPlatinum['date'], dfPlatinum['high'])
plt.plot(dfPalladium['date'], dfPalladium['high'])

plt.xlabel("Fecha")
plt.ylabel("Precio")

# Ajusta el formato de las fechas en el eje x
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# Ajusta el formato de las fechas en el eje x
plt.gcf().autofmt_xdate()
plt.savefig(os.path.join('plots', 'Paladio.png'))

plt.show()

