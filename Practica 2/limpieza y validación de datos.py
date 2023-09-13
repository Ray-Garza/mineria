import pandas as pd

#Dirección del archivo
archivo_csv = '../precious-metals-data/all_commodities_data.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(archivo_csv)

# Eliminar la columna "ticker" del DataFrame original
df.drop(columns=['ticker'], inplace=True)

# Imprimir los primeros valores
print(df.head())

#Validar si existen valores nulos o duplicados
valoresNulos = df.isnull()
print(valoresNulos.sum())
filasDuplicadas = df.duplicated()
print(filasDuplicadas.sum())

#Guardar archivo csv sin el índice y actualizarlo en caso de que ya exista
df.to_csv('MineralesLimpios.csv', index=False)


