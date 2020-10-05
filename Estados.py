# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:27:20 2020

@author: Isaac Bustamante
"""

import pandas as pd

#leemos el excel con un metodo de pandas
estados = pd.read_csv('C://Datos/estados.csv')

#Indices de una columna
#print(estados['ESTADO'])

#Junta dos columnas
#print(estados[{'NUMESTADO','ESTADO'}])

#Seleccionamos filas a imprimir
print(estados[0:5])

#print(diccionario)

    
