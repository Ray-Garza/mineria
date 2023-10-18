import pandas as pd
import matplotlib.pyplot as plt
"""
#Dirección del archivo
archivo_csv = 'Practica 2\MineralesLimpios.csv'

# Cargar el archivo CSV en un DataFrame
dfg = pd.read_csv(archivo_csv)

df = dfg.loc[dfg['commodity'] == 'Gold', ['date', 'close']]

# Convierte la columna 'date' a formato datetime
df['date'] = pd.to_datetime(df['date'])

# Grafica las fechas en el eje x y los valores 'close' en el eje y
plt.plot(df['date'], df['close'])

# Añade etiquetas a los ejes
plt.xlabel('Fecha')
plt.ylabel('Close Value')

# Ajusta el formato de las fechas en el eje x
plt.gcf().autofmt_xdate()

# Muestra el gráfico
plt.show()

"""

#Dirección del archivo
archivo_csv = 'Practica 2\MineralesLimpios.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(archivo_csv)
df['date'] = pd.to_datetime(df['date'])

#DataFrame de cada mineral
dfGold = df.loc[df['commodity'] == 'Gold', ['date', 'high']].reset_index(drop=True)
dfSilver = df.loc[df['commodity'] == 'Silver', ['date', 'high']].reset_index(drop=True)
dfCopper = df.loc[df['commodity'] == 'Copper', ['date', 'high']].reset_index(drop=True)
dfPlatinum = df.loc[df['commodity'] == 'Platinum', ['date', 'high']].reset_index(drop=True)
dfPalladium = df.loc[df['commodity'] == 'Palladium', ['date', 'high']].reset_index(drop=True)


dfM = pd.merge(dfGold, dfSilver, on='date', how='outer')
dfM = dfM.rename(columns={'high_x':'high_Gold', 'high_y':'high_Silver'})
dfM = pd.merge(dfM, dfCopper, on='date', how='outer')
dfM = pd.merge(dfM, dfPlatinum, on='date', how='outer')
dfM = dfM.rename(columns={'high_x':'high_Copper', 'high_y':'high_Platinum'})
dfM = pd.merge(dfM, dfPalladium, on='date', how='outer')
dfM = dfM.rename(columns={'high':'high_Palladium'})
dfM = dfM.fillna('0')




plt.figure(figsize=(10, 6))
plt.scatter(dfM['date'], dfM['high_Gold'], label='Oro', marker='o', s=5)
plt.scatter(dfM['date'], dfM['high_Silver'], label='Plata', marker='o', s=5)
plt.scatter(dfM['date'], dfM['high_Copper'], label='Cobre', marker='o', s=5)
plt.scatter(dfM['date'], dfM['high_Platinum'], label='Platino', marker='o', s=5)
plt.scatter(dfM['date'], dfM['high_Palladium'], label='Paladio', marker='o', s=5)


plt.xlabel('Fecha')
plt.ylabel('Valores')
plt.title('Valores a lo largo del tiempo')
plt.legend()

plt.show()
