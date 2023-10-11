import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import statsmodels.api as sm
import os

#Regresión lineal
def regresionLineal(df, columnaDate, columnaHigh, name):
    #Tamaño de la figura
    plt.figure(figsize=(10,8))

    #Plot de los puntos
    plt.scatter(df[columnaDate], df[columnaHigh],label = 'Datos', marker='o', s=5)

    #Regresion lineal
    df['date_numerico'] = df[columnaDate].apply(lambda x: x.toordinal())        
    X = sm.add_constant(df['date_numerico'])
    model = sm.OLS(df[columnaHigh], X).fit()
    print(name)
    print(model.summary())
    print('\n')
    Y = model.predict(X)


    #Plot de regresion lineal
    plt.plot(df[columnaDate], Y, label='Línea de Regresión' )

    # Ajusta el formato de las fechas en el eje x
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # Ajusta el formato de las fechas en el eje x
    plt.gcf().autofmt_xdate()

    #Tecnisismos
    plt.xlabel("Fecha")
    plt.ylabel("Precio")
    plt.title(name)
    plt.legend()
    plt.savefig(os.path.join('plots', 'Regresion Lineal '+name + '.png' ))
    plt.clf()

    

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


regresionLineal(dfGold,'date','high','Oro')
regresionLineal(dfSilver,'date','high','Plata')
regresionLineal(dfCopper,'date','high','Cobre')
regresionLineal(dfPlatinum,'date','high','Platino')
regresionLineal(dfPalladium,'date','high','Paladio')



