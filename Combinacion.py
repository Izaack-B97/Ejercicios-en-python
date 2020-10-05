# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:30:43 2020

@author: Isaac Bustamante
"""

#Elaborar un scrip que saque los numeros pares e impares de un array y saque sus respectivas media, mediana, moda

import numpy
from scipy import stats

array = [12,3,3,4,5,4,23,9,5,5,5,5,45,6,4,100,43,6,78,78,78]
array_impar = []
array_par = []
for i in array:
    if(i % 2 == 0):
        #print("Par: " , i)
        array_par.append(i)
    else:
        #print("Impar: ", i)
        array_impar.append(i)
print("Array de pares")
print(array_par)
print("Media: ", numpy.mean(array_par))
print("Mediana: ", numpy.median(array_par))
print("Moda: ", stats.mode(array_par))
print("-----------------------------------")
print("Array de impares")
print(array_impar)
print("Media: ", numpy.mean(array_impar))
print("Mediana: ", numpy.median(array_impar))
print("Moda: ", stats.mode(array_impar))