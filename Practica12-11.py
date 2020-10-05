# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:19:46 2020

@author: Isaac Bustamante

11.	Crearemos un script que generé las tres gráficas anteriormente aprendidas con información libre.
Nota: los alumnos deberán inventar la información y crear las matrices por ellos mismos.

"""

#Grafica que describe el mejor semestre con sus 
#calificaciones en el servicio
import matplotlib.pyplot as plt
"""
# MATRIZ CON LOS MESES DE MEJOR SEVICIO
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]

# MATRIZ CON LAS CALIFICACIONES DEL PRIMER SEMESTRE
calificaciones = [3.6, 4.6, 3.8, 4.0, 5.12, 4.53]

# DIBUJAMOS EL GRAFICO
plt.stem(meses, calificaciones, use_line_collection = True)

# MOSTRAMOS EL GRAFICO
plt.show()"""


""" *** GRAFICA DE BARRAS CON ROTULOS INCLINADOS *** """
#Matriz con los comerciales de abarrotes mas comunes
candidatos = ['Ley', 'Soriana', 'Bodega Aurrera', 'Walmart', 'Leyva']

#Matriz con las ganancias en millones
ganancias_empresa = [4.2, 25.2, 21.9, 30.9, 3.2]

#Dibujamos el grafico
plt.bar(range(5), ganancias_empresa, edgecolor = 'red', color = 'm')

#Indicamos los rotulos del eje x con propieades
plt.xticks(range(5), candidatos, rotation = 60)

#Indicamos el titulo del grafico
plt.title('Ganancias segun la empresa')

#Indicamos los valores del eje y 
plt.ylim(min(ganancias_empresa)-1, max(ganancias_empresa)+1)

#Mostramos el grafico
plt.show()

""" *** GRAFICO DE ESCALERAS *** """
 
#Promedios generales de la escuela primaria niños heroes
"""
#Matriz con los años de primaria
grados = ["1ero", "2do", "3ro", "4to", "5to", "6to"]

#Matriz con los promedio generales del grupo 
promedios = [9.5,7.8,9.6,7.6,10,10]

#Dibujamos el grafico
plt.step(grados, promedios)

#Indicamos el titulo del grafico
plt.title("Promedios de los grados de la escuela Niños Heroes 2020")

#Indicamos el titulo del eje x
plt.xlabel("Grados")

#Indicamos los rotulos del eje x con sus propiedades 
plt.xticks(range(6), grados, rotation = 90)

#Mosytramos el graficop
plt.show()
"""