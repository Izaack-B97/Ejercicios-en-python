# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:42:26 2020

@author: Isaac Bustamante

8.	Crearemos un script que generé las tres gráficas anteriormente aprendidas con información libre.
Nota: los alumnos deberán inventar la información y crear las matrices por ellos mismos.

"""

import matplotlib.pyplot as plt
import numpy as np







#Personas que tocan instrumentos
"""#Matriz con los instrumentos
instrumentos = ["Piano", "Guitarra", "Violin", "Acordion", "Flauta"]

#Indicamos el tamaño del eje de y 
posicion_y = np.arange(len(instrumentos))

#Matriz con las cantidad de preferencia por sabor de helado
personas = [ 500, 343, 990, 232, 120]

#Dibujamos el grafico
plt.barh(posicion_y, personas, align = "center")

#Indicamos los rotulos dele eje y 
#(tamaño, rotulos)
plt.yticks(posicion_y, instrumentos)

#Titulo de eje en y
plt.ylabel("Intrumentos")

#Titulo de eje en x
plt.xlabel("No. Personas que tocan")

#Titulo del grafico
plt.title("Preferencia de instrumentos en las personas")

"""

#GRAFICA DE BARRAS DOBLES . Vuelos Satisfactorios en tiempo y tardios

"""
# [Vuelos que salieron a tiempo][Vuelos que salieron fuera de tiempo]
datos = [[10, 11, 20], [5, 15, 3]]

#Indicamos el tamaño del eje x
x = np.arange(3)

# Dibujamos las 3 barras de los vuelos que salieron a tiempo
plt.bar(x + 0.00, datos[0], color = 'b', width = 0.30) 

# Dibujamos las 3 barras de los vuelos que salieron tardios
plt.bar(x + 0.25, datos[1], color = 'm', width = 0.30) 

#Rotulos del eje x
#(posicion, [rotulos])
plt.xticks(x + 0.12, ["Volaris", "Viva aerobus", "Interjet"])

#Titulo del eje x
plt.xlabel("Aerolineas")

#Titulo del eje y 
plt.ylabel("Vuelos")

#Titulo de la grafica
plt.title("Cantidad de Vuelos a Tiempo y Tardios")"""

#--------------------------------------------

""" *** GRAFICA DE PASTEL *** """

# Matriz con la cantidad  de promedios de los niños de primaria de primero a sexto
promedios = [70.6, 52.6, 60.0, 55.6, 43.6, 23.3]

# Matriz con los grados de primaria
grados = ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto', 'Sexto']

#Destacamos el grado mas alto
explode = [0.2, 0, 0, 0, 0, 0]

#Dibujamos el grafico 
plt.pie(promedios, labels = grados, explode = explode, autopct = '%1.1f%%', shadow = True, startangle = 100)

#Titulo del grafico
plt.title("Calificaciones de los grados de primaria")



