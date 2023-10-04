import pandas as pd
import matplotlib.pyplot as plt

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