# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:35:13 2020

@author: Isaac Bustamamnte
"""

#Haremos un histograma


import numpy
import matplotlib.pyplot as plt
x = numpy.random.uniform(0.0, 1.0, 250)
print(x)

plt.hist(x, 5)

plt.title("Numeros Flotantes generados")

plt.ylabel("Cantidad")

plt.show()
