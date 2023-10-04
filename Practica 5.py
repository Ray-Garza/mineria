import pandas as pd
from scipy.stats import f_oneway


#Dirección del archivo
archivo_csv = 'Practica 2\MineralesLimpios.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(archivo_csv)
df['date'] = pd.to_datetime(df['date'])

#DataFrame de cada mineral
dfGold = df.loc[df['commodity'] == 'Gold', ['date', 'high']]
dfSilver = df.loc[df['commodity'] == 'Silver', ['date', 'high']]
dfCopper = df.loc[df['commodity'] == 'Copper', ['date', 'high']]
dfPlatinum = df.loc[df['commodity'] == 'Platinum', ['date', 'high']]
dfPalladium = df.loc[df['commodity'] == 'Palladium', ['date', 'high']]


#Aqui voy a analizar las medias de cada mineral y ver si son diferentes
#(Spoiler: Si son diferentes)


# Valores de 'high' para cada mineral
gold = dfGold['high']
silver = dfSilver['high']
copper = dfCopper['high']
platinum = dfPlatinum['high']
palladium = dfPalladium['high']

# Realizar el ANOVA
f_stat, p_value = f_oneway(gold, silver, copper, platinum, palladium)

# Imprime los resultados
print("Prueba que analiza las medias de los minerales")
print(f'Estadistico F: {f_stat}')
print(f'Valor p: {p_value: }')

# Comprueba la significancia
alpha = 0.05
if p_value < alpha:
    print('Las medias de    los minerales son diferentes (rechazamos la hipotesis nula)\n')
else:
    print('No hay evidencia suficiente para decir que las medias de los minerales son diferentes (no rechazamos la hipótesis nula)\n')


#Aqui me enfoqué únicamente en los valores del oro, y dividí los datos en 6 intervalos de tiempo:
#Un grupo con los valores del 2000 al 2003, otro del 2004 al 2007 y así
#Hice un ANOVA para verificar si la media había cambiado con el tiempo
#(Spoiler: si cambió)

# Definir el rango de años
inicio = 2000
fin = 2023
intervalo_anios = 4

# Crear una lista para almacenar los DataFrames fragmentados
grupos = []

# Fragmentar el DataFrame en intervalos de 4 años
for i in range(inicio, fin, intervalo_anios):
    inicio_intervalo = f"{i}-01-01"
    fin_intervalo = f"{i + intervalo_anios - 1}-12-31"
    grupo = dfGold[(dfGold['date'] >= inicio_intervalo) & (dfGold['date'] <= fin_intervalo)]
    grupos.append(grupo)

# Valores 'high' de cada grupo
valores_grupos = [grupo['high'] for grupo in grupos]

# Realiza el ANOVA
f_stat, p_value = f_oneway(*valores_grupos)

# Imprime los resultados
print("Prueba que analiza las medias del oro en diferentes intervalos de tiempo")
print(f'Estadistico F: {f_stat}')
print(f'Valor p: {p_value}')

# Comprueba la significancia
alpha = 0.05
if p_value < alpha:
    print('Las medias del oro dividido en 6 intervalos de tiempo son diferentes (rechazamos la hipotesis nula)')
else:
    print('No hay evidencia suficiente para decir que las medias del oro dividido en 6 intervalos de tiempo son diferentes (no rechazamos la hipótesis nula)')