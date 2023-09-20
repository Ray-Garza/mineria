import pandas as pd

#Dirección del archivo
archivo_csv = 'Practica 2\MineralesLimpios.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(archivo_csv)

#Para probar estos estadísticos, pensé que sería mejor utilizar
#el año mas reciente
dfActual = df[df['date'] >= '2023-01-01']
#print(dfActual.head())

#Encontrar los valores maximos de venta de cada mineral en el año
print("Valores de venta más altos del 2023")
print(dfActual.groupby('commodity')['high'].max())
print("\n")

#Encontrar los valores minimos de venta de cada mineral en el año
print("Valores de venta más bajos del 2023")
print(dfActual.groupby('commodity')['low'].min())
print("\n")

#Encontrar la media de los valores de salida de venta de cada mineral en el año
print("Valores de venta medios del 2023")
print(dfActual.groupby('commodity')['open'].mean())
print("\n")

#Encontrar la desviación de los valores de salida de venta de cada mineral en el año
print("desviación estándar de los valores de venta del 2023")
print(dfActual.groupby('commodity')['open'].std())
print("\n")