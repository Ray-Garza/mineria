import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np  
import os

#Dirección del archivo
archivo_csv = 'Practica 2\MineralesLimpios.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(archivo_csv)
df['date'] = pd.to_datetime(df['date'])
dfActual = df[df['date'] >= '2023-01-01']

#Permuté los datos para que no estuvieran en orden
dfPrecioPermutado = np.random.permutation(dfActual[['high']])

#Arreglo que guarda la suma del cuadrado de las distancias
sumaDeLasDistancias = []

#Se hace el algoritmo kmeans con k desde el 1 al 10
for k in range(1,10):
    kmeans = KMeans(n_clusters = k, random_state=0, n_init=5)
    kmeans.fit_predict(dfPrecioPermutado)
    sumaDeLasDistancias.append(kmeans.inertia_)        
    plt.scatter(list(range(len(dfPrecioPermutado))), dfPrecioPermutado, c=kmeans.labels_)
    plt.savefig(os.path.join('plots/cluster','Kmeans con K ='+str(k)))
    plt.clf()
    
# Graficar la suma de cuadrados de distancias en función de n_clusters
plt.plot(range(1,10), sumaDeLasDistancias, 'bx-')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('Suma de Cuadrados de Distancias')
plt.title('Método del Codo para Determinar k')
plt.savefig(os.path.join('plots/cluster', 'Metodo del codo de Kmeans'))




