# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:26:22 2020

@author: DELL
"""
import numpy

#Importaremos la libreria matplotlib
import matplotlib.pyplot as plt

#Crearemos la matriz normal
#(Valor media, desviacion estandar, varianza)
x = numpy.random.normal(5.0,1.0,100000)

#Centraremos el histograma (matriz, numero de barras,)
plt.hist(x,100)
#Mostramos la grafica
plt.show()