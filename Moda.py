# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:18:25 2020

@author: DELL
"""

#Importamos la libreria Scipy
from scipy import stats

#Creamos el arreglo
moda = [10, 4, 6, 9, 6, 8, 9, 1, 9, 6, 9, 4]

#Creamos la variable donde guardar el calculo
x = stats.mode(moda)#Saca la moda en el arreglo

print("El numero de moda es: ",x)