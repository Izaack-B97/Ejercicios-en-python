# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:14:34 2020

@author: DELL
"""
#Imortamos la libreria
import numpy

#Creamos el arreglo
tallas = [3, 5, 2, 6, 5, 9, 5, 2, 8]

#Creamos una variable dondeguardar el calculo
x = numpy.median(tallas)#Saca la mediana en un array

#Imprimimos el resultado
print("La mediana es ", x)
