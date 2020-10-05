# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:23:33 2020

@author: Isaac Bustamante
"""

"""
Crearemos un script que lea el archivo "financiamiento" y lo analizaremos una columna en especifico
"Monto del credito en pesos" con todos los conceptos vistos de estadisticas hasta ahorita como por ejempplo
media, mediana, moda, desviacion estandar, varianza, percentiles, distribucion de datos, y generar un histograma 
"""

import pandas as pd
import numpy
import matplotlib.pyplot as plt
from scipy import stats

"""df = pd.read_csv('C://Datos/Financiamiento2016.csv', encoding='cp1252')
#print(df[{'Monto del credito en pesos','Entidad Federativa'}])

#Sacamos los estados unicos
array_estados = df['Entidad Federativa'].unique()

#Convertimos la columna Monto del credito en pesos en un array
array_pesos = []
for i in df['Monto del credito en pesos']:
    array_pesos.append(i)

#print(array_pesos)    
#print(array_estados)
    
#Sacamos las estadisticas
media = numpy.mean(array_pesos)
mediana = numpy.median(array_pesos)
moda = stats.mode(array_pesos)
varianza = numpy.var(array_pesos)
desviacion_estandar = numpy.std(array_pesos)
percentil = numpy.percentile(array_pesos, 40)

#Imprimimos las estadisticas
print("Media: ", media)
print("Mediana: ", mediana)
print("Moda: ", moda)
print("Varianza: ", varianza)
print("Desviacion estandar: ",desviacion_estandar)
print("Percentil: ", percentil)

#Creamos el histograma
plt.hist(array_pesos, 5)
plt.title("Monto del credito en pesos")
plt.ylabel('Monto')

#plt.bar(array_estados, array_pesos, width=0.4)
#plt.xticks(array_estados)
#plt.show()

fig = plt.figure(u'Gráfica de barras') # Figure
ax = fig.add_subplot(111) # Axes

nombres = ['Juan','Ana','Pablo','Ximena','Jorge']
datos = [media,mediana,varianza,desviacion_estandar,percentil]
xx = range(len(datos))

ax.bar(xx, datos, width=0.8, align='center')
ax.set_xticks(xx)
ax.set_xticklabels(nombres)

plt.show()"""


df = pd.read_csv("C://Datos/Financiamiento2016.csv", encoding="cp1252")
pesos = df['Monto del credito en pesos']

#Sacamos las estadisticas
media = numpy.mean(pesos)
mediana = numpy.median(pesos)
moda = stats.mode(pesos)
varianza = numpy.var(pesos)
desviacion_estandar = numpy.std(pesos)
percentil = numpy.percentile(pesos, 40)

#Imprimimos las estadisticas
print("Media: ", media)
print("Mediana: ", mediana)
print("Moda: ", moda)
print("Varianza: ", varianza)
print("Desviacion estandar: ",desviacion_estandar)
print("Percentil: ", percentil)

datos = [media,mediana,desviacion_estandar,percentil]
nombres = ['Media','Mediana','Desviacion Estandar','Percentiles']

fig = plt.figure(u'Gráfica de barras') # Figure
ax = fig.add_subplot(111) # Axes
xx = range(len(datos))
ax.bar(xx, datos, width=0.8, align='center')
ax.set_xticks(xx)
ax.set_xticklabels(nombres)
plt.show()

plt.show()

#print(df)







