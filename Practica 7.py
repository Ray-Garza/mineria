import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

#Dirección del archivo
archivo_csv = 'Practica 2\MineralesLimpios.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(archivo_csv)
df['date'] = pd.to_datetime(df['date'])
dfActual = df[df['date'] >= '2023-01-01']

dfEtiqueta = dfActual[['commodity', 'high']]


#plt.scatter(dfEtiqueta['commodity'], dfEtiqueta['high'])
#plt.show()


knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(dfEtiqueta['high'].values.reshape(-1,1), dfEtiqueta['commodity'],)


#Datos de prueba a predecir
X_test = [
    [3], #Cobre
    [2000], #Oro
    [1800], #Oro
    [1400], #Paladio
    [900], #Platino
    [20], #Plata
    [1550], #Paladio
    [2200], #Oro
    [2400], 
    [5000]
]

print(knn.predict(X_test))


