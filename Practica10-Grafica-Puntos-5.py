# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 16:13:26 2020

@author: DELL
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Leemos el archivo inmuebles
inmueble_data = pd.read_csv("C://Datos/Inmuebles.csv")


frecuencias = [0,0,0,0]
provincias = inmueble_data['Provincia'].unique()

print(provincias)


for i in range(0,len(provincias)):
    for j in inmueble_data['Provincia']:
        if(provincias[i] == j):
            frecuencias[i] += 1

#print(frecuencias)

array_numpy = np.array(frecuencias)
#print(array_numpy)

plt.plot(array_numpy, marker='*', color='k', label = 'Provincias Rentadas 2004 - 2007', linestyle = '-')
plt.title("Frecuencia de provincias rentadas")
plt.xlabel("Provincias")
plt.ylabel("No. Rentas")

plt.legend()

indice = np.arange(4)
plt.xticks(indice,provincias)

plt.yticks(0,110,10)
