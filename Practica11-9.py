# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:14:08 2020

@author: Isaac Bustamante

9.	Crearemos un script que lea el archivo “Inmuebles.csv” y generaremos las tres diferentes 
gráficas aprendidas anteriormente con información obtenida del archivo csv.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("C://Datos/Inmuebles.csv");

""" *** GRAFICA DE BARRAS HORIZONTALES *** """

#   Esta tabla define cual es el inmueble que mas se gasta en las 
#   diferentes tipo de ventas de inmuebles

"""tipo_inmueble = data['Tipo'].unique()
precio_ventas =  [0,0,0,0,0,0,0]
#print(precio_ventas)

for i in range(0,len(tipo_inmueble)):
    for j, row in data.iterrows():
        if (tipo_inmueble[i] == row['Tipo']):
            precio_ventas[i] += row['Precio Venta']       

print(precio_ventas)

#Indicamos el tamaño del eje de y 
posicion_y = np.arange(len(tipo_inmueble))


#Dibujamos el grafico
plt.barh(posicion_y, precio_ventas, align = "center")

#Indicamos los rotulos dele eje y 
#(tamaño, rotulos)
plt.yticks(posicion_y, tipo_inmueble)

#Titulo de eje en y
plt.ylabel("Tipo Inmueble")

#Titulo de eje en x
plt.xlabel("Precio Venta")

#Titulo del grafico
plt.title("Precio venta de los tipos de imuebles")
"""

""" *** GRAFICA DE BARRAS DOBLES *** """
#   Esta grafica es para ver la comparacion de superfie precios por provincias 
#    de una muestra de 10 entidades

#Tomatos como muestra las primeras 10 provincias
provincias = data.loc[:10,'Provincia'].unique()
diccionario = []
precios = []#   aqui iran la superficie y el precio venta totales de cada provincia
superficies = []

# Iteramos las provincias unicas
"""for i in range(0,len(provincias)):
    precio_venta  = 0
    superficie = 0
    for j,row in data[0:10].iterrows():#   Iteramos los primeros 10 renglones
        if(provincias[i] == row['Provincia']):
            precio_venta += (row['Precio Venta'])#    Acumulamos el precio vent
            superficie += (row['Superficie'])#    Acumulamos la superficie de la provincia
                    
    superficies.append(superficie*10);#    Agregamos la superficie y la multiplicamos por 10 para poder visualizar al barra azul
    precios.append(precio_venta/1000)#   Agregamos el precio venta y la dividimos entre 1000 para poder viziualizar la barra magenta
    
    #diccionario.append(superficies)#    Agregamos el arreglo al diccionario
    #diccionario.append(precios)
print(superficies)
print(precios)
diccionario.append(superficies)
diccionario.append(precios)

print(provincias)

#Indicamos el tamaño del eje x
x = np.arange(3)

# Dibujamos las 3 barras de las superficies
plt.bar(x + 0.00, diccionario[0], color = 'b', width = 0.30) 

# Dibujamos las 3 barras de los precio ventas
plt.bar(x + 0.25, diccionario[1], color = 'm', width = 0.30) 

#Rotulos del eje x
#(posicion, [rotulos])
plt.xticks(x + 0.12, provincias)

#Titulo del eje x
plt.xlabel("Superficie Precio")

#Titulo del eje y 
plt.ylabel("Cantidad")

#Titulo de la grafica
plt.title("Comparacion de precios superficie de una muestra de 10")"""

#--------------------------------------------

""" *** GRAFICA DE PASTEL *** """


tipo_inmueble = data['Tipo'].unique()
print(tipo_inmueble)

totales = [0, 0, 0, 0, 0, 0, 0]

for i in range(0, len(tipo_inmueble)):
    for j, row in data[0:100].iterrows():
        if(tipo_inmueble[i] == row['Tipo']):
            totales[i] += row['Precio Venta']
            
#print(totales)

#Destacamos el grado mas alto
explode = [0, 0, 0, 0, 0, 0.5, 0]

#Dibujamos el grafico 
plt.pie(totales, labels = tipo_inmueble, explode = explode, autopct = '%1.1f%%', shadow = True, startangle = 100)

#Titulo del grafico
plt.title("Precios totales de una muestra de 100 de inmuebles")