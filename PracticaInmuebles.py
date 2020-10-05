# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:39:07 2020

@author: Isaac Bustamante
"""
#Crearemos un script que lea el archivo "Inmuebles.csv" y lo analizaremos, existen columnas
#que se pueden analizar con todos los conceptos visto de estadistica hasta ahorita como por 
#ejemplo , media, mediana. moda, desviacion estandar, percentiles, distribucion de datos y  
#genera el histograma, repasando algunas anetiores vistas en clases


import numpy 
from scipy import stats 
import pandas
import matplotlib.pyplot as plt

#Leemos el archivo
inmueble_data = pandas.read_csv("C://Datos/Inmuebles.csv")
#print(inmueble_data)

#Estadisticas de las superficies
media_s = numpy.mean(inmueble_data['Superficie'])
mediana_s = numpy.median(inmueble_data['Superficie'])
moda_s = stats.mode(inmueble_data['Superficie'])
varianza_s = numpy.var(inmueble_data['Superficie'])
desviacion_estandar_s = numpy.std(inmueble_data['Superficie'])
percentil_s = numpy.percentile(inmueble_data['Superficie'], 40)

print('Estatidisticas de la dispersion de datos en Superficie')
print("\tMedia: ", media_s)
print("\tMediana: ", mediana_s)
print("\tModa: ", moda_s)
print("\tVarianza: ", varianza_s)
print("\tDesviacion estandar: ",desviacion_estandar_s)
print("\tPercentil: ", percentil_s)

print('------------------------------------------------------------------------------')

#Estadisticas sobre el precio de venta
media_pv = numpy.mean(inmueble_data['Precio Venta'])
mediana_pv = numpy.median(inmueble_data['Precio Venta'])
moda_pv = stats.mode(inmueble_data['Precio Venta'])
varianza_pv = numpy.var(inmueble_data['Precio Venta'])
desviacion_estandar_pv = numpy.std(inmueble_data['Precio Venta'])
percentil_pv = numpy.percentile(inmueble_data['Precio Venta'], 40)

print('Estadisticas de la dispersion de datos en en el Precio Venta de la superficie')
print("\tMedia: ", media_pv)
print("\tMediana: ", mediana_pv)
print("\tModa: ", moda_pv)
print("\tVarianza: ", varianza_pv)
print("\tDesviacion estandar: ",desviacion_estandar_pv)
print("\tPercentil: ", percentil_pv)

#Generaremos el histograma de frecuencias con base en la provincia 
#en la que se esta rentando

frecuencias = [0,0,0,0]

provincias = inmueble_data['Provincia'].unique()

for i in range(0,len(provincias)):
    for j in inmueble_data['Provincia']:
        if(provincias[i] == j):
            frecuencias[i] += 1 

print("FRECUENCIAS")
print (frecuencias);
print("\n")
print("***HISTOGRAMA DE FRECUENCIAS SEGUN LA PROVINCIA QUE SE RENTA***")

fig = plt.figure(u'Gráfica de barras') # Figure
ax = fig.add_subplot(111) # Axes
xx = range(len(frecuencias))
ax.bar(xx, frecuencias, width=0.7, align='center')
ax.set_xticks(xx)
ax.set_xticklabels(provincias)
plt.show()

#print(provincias)