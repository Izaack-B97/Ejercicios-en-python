# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:39:57 2020

@author: Isaac Bustamante

12.	Crearemos un script que lea el archivo “Inmuebles.csv” y 
generaremos las tres diferentes gráficas aprendidas anteriormente con 
información obtenida del archivo csv.
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C://Datos/Inmuebles.csv")
print(df)


provincias = df['Provincia'].unique()
superficies = [0, 0, 0, 0]

for i in range(0, len(provincias)):
    for j, rows in df[:100].iterrows():
        if(provincias[i] == rows['Provincia']):
           superficies[i] += rows['Superficie']

#print(superficies)
           
""" GRAFICA DE LINEAS Y PUNTOS """

"""# DIBUJAMOS EL GRAFICO
plt.stem(provincias, superficies, use_line_collection = True)
# DEFINIMOS EL TITULO
plt.title("Terreno total de una muestra de 10")
plt.xlabel("Provincias")
plt.ylabel("Cantidad - Superficie")
# MOSTRAMOS EL GRAFICO
plt.show()
"""


"""GRAFICA DE BARRAS CON ROTULOS INCLINADOS"""
"""#Dibujamos el grafico
plt.bar(range(4), superficies, edgecolor = 'red', color = 'k')

#Indicamos los rotulos del eje x con propieades
plt.xticks(range(4), provincias, rotation = 70)

#Indicamos el titulo del grafico
plt.title('Superficie por provincia de una muestra de 100')

#Indicamos los valores del eje y 
plt.ylim(min(provincias)-1, max(superficies)+1)

#Mostramos el grafico
plt.show()"""


""" ***GRAFICA DE ESCALERA*** """
#Dibujamos el grafico
plt.step(provincias, superficies)

#Indicamos el titulo del grafico
plt.title("Superficie por provincia de una muestra de 100")

#Indicamos el titulo del eje x
plt.xlabel("Provincias")

#Indicamos los rotulos del eje x con sus propiedades 
plt.xticks(range(4), provincias, rotation = 90)

#Mosytramos el graficop
plt.show()
