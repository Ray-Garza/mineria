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


"""import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import os

#Dirección del archivo
archivo_csv = 'Practica 2\MineralesLimpios.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(archivo_csv)
df['date'] = pd.to_datetime(df['date'])
dfGold = df.loc[df['commodity'] == 'Gold', ['date', 'high']]
dfGold['date_numerico'] = df['date'].apply(lambda x: x.toordinal())  

# Definir el rango de años
inicio = 2001
fin = 2024
intervalo_anios = 4

# Crear una lista para almacenar los DataFrames fragmentados
grupos = []

# Fragmentar el DataFrame en intervalos de 4 años
for i in range(inicio, fin, intervalo_anios):
    inicio_intervalo = f"{i}-01-01"
    fin_intervalo = f"{i + intervalo_anios - 1}-12-31"
    grupo = dfGold[(dfGold['date'] >= inicio_intervalo) & (dfGold['date'] <= fin_intervalo)]
    grupos.append(grupo)

#Tamaño de la figura
plt.figure(figsize=(10,8))

#Plot de los puntos
plt.scatter(dfGold['date'], dfGold['high'], s=1)
plt.xlabel("Fecha")
plt.ylabel("Precio")
plt.title("Oro")

#Lista de colores del plot
colores = ['red', 'gray', 'green', 'orange', 'purple', 'pink']

#Regresión lineal 
for i in range(6):        
    X = sm.add_constant(grupos[i]['date_numerico'])
    model = sm.OLS(grupos[i]['high'], X).fit()
    Y = model.predict(X)
    predictions = model.get_prediction(X)
    pred_ci = pd.DataFrame(predictions.conf_int(), columns=['lower', 'upper'])  # Convertir a DataFrame
    

    # Plot de regresión lineal
    plt.plot(grupos[i]['date'], Y, label=f'Línea de Regresión {i+1}', color=colores[i], linewidth=3.0)

    # Área de desviación estándar
    plt.fill_between(grupos[i]['date'], pred_ci['lower'], pred_ci['upper'], color=colores[i], alpha=0.3)        

plt.savefig(os.path.join('plots', 'Forecasting Oro.png' ))
plt.show()"""

"""import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import os

#Dirección del archivo
archivo_csv = 'Practica 2\MineralesLimpios.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(archivo_csv)
df['date'] = pd.to_datetime(df['date'])
dfGold = df.loc[df['commodity'] == 'Gold', ['date', 'high']]
dfGold['date_numerico'] = df['date'].apply(lambda x: x.toordinal())  

# Definir el rango de años
inicio = 2001
fin = 2024
intervalo_anios = 4

# Crear una lista para almacenar los DataFrames fragmentados
grupos = []

# Fragmentar el DataFrame en intervalos de 4 años
for i in range(inicio, fin, intervalo_anios):
    inicio_intervalo = f"{i}-01-01"
    fin_intervalo = f"{i + intervalo_anios - 1}-12-31"
    grupo = dfGold[(dfGold['date'] >= inicio_intervalo) & (dfGold['date'] <= fin_intervalo)]
    grupos.append(grupo)

#Tamaño de la figura
plt.figure(figsize=(10,8))

#Plot de los puntos
plt.scatter(dfGold['date'], dfGold['high'], s=1)
plt.xlabel("Fecha")
plt.ylabel("Precio")
plt.title("Oro")

#Lista de colores del plot
colores = ['red', 'gray', 'green', 'orange', 'purple', 'pink']

#Regresión lineal 
for i in range(6):        
    X = sm.add_constant(grupos[i]['date_numerico'])
    model = sm.OLS(grupos[i]['high'], X).fit()
    Y = model.predict(X)
    
    std_dev = np.std(model.resid)  # Desviación estándar de los residuos

    # Plot de regresión lineal
    plt.plot(grupos[i]['date'], Y, label=f'Línea de Regresión {i+1}', color=colores[i], linewidth=3.0)

    # Área de desviación estándar
    plt.fill_between(grupos[i]['date'], Y - std_dev, Y + std_dev, color=colores[i], alpha=0.3)        
plt.savefig(os.path.join('plots', 'Forecasting Oro std.png' ))
plt.show()"""
