# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:25:08 2020

@author: Isaac Bustamante
14.	Crearemos un script que en Spyder, para generar un gráfico donde nos muestre la cantidad de personas 
tituladas y no tituladas.
Nota: Entregado significa que la persona ya esta titulad@, si nos aparece algo diferente significa que 
no esta titulad@ aún.

"""
# Importamos pandas
import pandas as pd

import numpy as np

#Importamos
import matplotlib.pyplot as plt

dt = pd.read_csv("C://Datos/DATOS_TITULO.csv");
countUnTitle = countTitle = 0
etiquetas = ["Titulados", "No Titulados"]
#print(dt)

for x in dt['TITULADO']:
    if(x == "Entregado"):
        countTitle += 1
    else:
        countUnTitle += 1

print(countUnTitle)
print(countTitle)

datos = [countTitle, countUnTitle]

fig = plt.figure(u'Gráfica de barras') # Figure
ax = fig.add_subplot(111) # Axes
xx = range(len(datos))
ax.bar(xx, datos, width=0.8, align='center')
ax.set_xticks(xx)
ax.set_xticklabels(etiquetas)
plt.show()
