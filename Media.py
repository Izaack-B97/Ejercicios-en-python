# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:10:43 2020

@author: DELL
"""

#importamos la libreria 
import numpy #Liberia que brinda soporte para arreglos y matrices

#Creamos un arreglo
calificaciones = [100, 90, 75, 96, 88, 95, 90, 60]

#Creamos la variable donde se guardara el calculo
x = numpy.mean(calificaciones)#numpy.mean saca la media en un arreglo

#Imprimimos el resultado
print("Promedio de calificaciones: ", x)