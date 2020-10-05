# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:13:46 2020

@author: Isaac Bustamante
"""
""" *** HISTOGRAMA VERTICAL *** """
#Importamos la libreria matplotlib
import matplotlib.pyplot as plt

#Importamos la libreria Numpy
import numpy as np 
"""
#Matriz con los sabores de helado
sabores = ["Vainilla", "Chocolate", "Fresa", "Pistache"]

#Indicamos el tamaño del eje de y 
posicion_y = np.arange(len(sabores))

#Matriz con las cantidad de preferencia por sabor de helado
personas = [342, 350, 278, 30]

#Dibujamos el grafico
plt.barh(posicion_y, personas, align = "center")

#Indicamos los rotulos dele eje y 
#(tamaño, rotulos)
plt.yticks(posicion_y, sabores)

#Titulo de eje en y
plt.ylabel("Sabores de helado")

#Titulo de eje en x
plt.xlabel("Cantidad de Preferencia")

#Titulo del grafico
plt.title("Sabores de helado preferente")
"""

#---------------------------------------

""" *** HISTOGRAMA HORIZONTAL CON DOBLE BARRAS HORIZONTALES *** """

"""# Matriz con los datos de cantidad de sexo por carrera en un grupo x
# M[ISS, ISI, IM], F[ IIS, ISI, IM]
datos = [[19, 13, 15], [15, 3, 9]]

#Indicamos el tamaño del eje x
x = np.arange(3)

# Dibujamos las 3 barras del sexo M
plt.bar(x + 0.00, datos[0], color = 'b', width = 0.25) 

# Dibujamos las 3 barras del sexo M
plt.bar(x + 0.25, datos[1], color = 'm', width = 0.25) 

#Rotulos del eje x
#(posicion, [rotulos])
plt.xticks(x + 0.12, ["IIS", "ISI", "IM"])

#Titulo del eje x
plt.xlabel("Sexo")

#Titulo del eje y 
plt.ylabel("Cantidad de personas")

#Titulo de la grafica
plt.title("Cantidad de personas por Sexo en los Grupos de 5to semestres")"""

#--------------------------------------

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
