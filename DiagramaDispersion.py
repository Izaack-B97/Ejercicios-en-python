# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:30:27 2020

@author: DELL
"""
#Crearemos la libreria matplotlib
import matplotlib.pyplot as plt
import numpy

#Crearemos la matriz con edades de automoviles
#x = {5,7,8,7,2,17,2,9,4,11,12,9,6}

#Crearemos la matriz con velocidades de los automoviles
#y = {99,86,87,88,111,86,103,87,94,78,77,85,86}

#Generaremos el diagrama de dispersion
#plt.scatter(x,y)

#Crearemos la matriz x
x = numpy.random.normal(5.0, 1.0, 1000)

#Crearemos la matriz y
y = numpy.random.normal(10.0, 2.0, 1000)

#Generaremos el diagrama de dispersion
plt.scatter(x,y)

#Mostramos el diagrama
plt.show()

