# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:34:17 2020

@author: Isaac Bustamante

"""
#Sacaremos el percentil
import numpy
edades = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
x = numpy.percentile(edades, 40)
print(x)

