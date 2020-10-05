# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:33:16 2020

@author: Isaac Bustamante
"""

""" *** GRAFICA DE LINEAS VERTICALES *** """
# IMPORTAMOS LA LIBRERIA MATLPLOT
import matplotlib.pyplot as plt

"""# MATRIZ CON LOS AÑOS DE DE LAS VENTAS
años = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

# MATRIZ CON LAS CANTIDADES DE VENTAS EN MILES POR AÑOS
ventas = [344, 467, 378,  437, 512, 453, 435, 467, 783, 790]

# DIBUJAMOS EL GRAFICO
plt.stem(años, ventas, use_line_collection = True)

# MOSTRAMOS EL GRAFICO
plt.show()
"""

""" *** GRAFICA DE BARRAS CON ROTULOS INCLINADOS *** """
"""#Matriz con los apelllidos de los candidatos
candidatos = ['Lopez Obrador', 'Anaya', 'Made', 'Zavala', 'Otros']

#Matriz con los porcentajes de votos en numeros
porcvotos = [40.2, 28.2, 21.9, 5.6, 3.2]

#Dibujamos el grafico
plt.bar(range(5), porcvotos, edgecolor = 'black')

#Indicamos los rotulos del eje x con propieades
plt.xticks(range(5), candidatos, rotation = 60)

#Indicamos el titulo del grafico
plt.title('Porcentajes de Votos')

#Indicamos los valores del eje y 
plt.ylim(min(porcvotos)-1, max(porcvotos)+1)

#Mostramos el grafico
plt.show()"""

""" *** GRAFICO DE ESCALERAS *** """

#Matriz con los meses de ventas
meses = ["Enero", "Febrero", "MArzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", 
         "Octubre", "Noviembre", "Diciembre"]

#Matriz con las cantidades de ventas en miles por año 
ventas = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#Dibujamos el grafico
plt.step(meses, ventas)

#Indicamos el titulo del grafico
plt.title("Dias por mes en el Año 2020")

#Indicamos el titulo del eje x
plt.xlabel("Meses")

#Indicamos los rotulos del eje x con sus propiedades 
plt.xticks(range(12), meses, rotation = 90)

#Mosytramos el graficop
plt.show()