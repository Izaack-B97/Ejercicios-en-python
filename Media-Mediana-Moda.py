# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:22:17 2020

@author: DELL
"""

"""
    Creamos un script que calcule la media, mediana y moda de las edades que existen en tu grupo.
    21,22,21,22,22,25,22,24,23,26,25,23
"""
#Importamos las librerias
import numpy
from scipy import stats

#Creamos el arreglo
arreglo = [21,22,21,22,22,25,22,24,23,26,25,23]

media = numpy.mean(arreglo)
mediana = numpy.median(arreglo)
moda = stats.mode(arreglo)

print("La media es: ", media)
print("LA mediana es: ", mediana)
print("La moda es: ", moda)
