# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 18:37:00 2020

@author: DELL
"""
import pandas as pd

#Creamos un directorio
dict = {
    "marca": ["Ford", "Toyota", "Chevrolet", "Volksvagen"],
    "modelo": ["Escape", "Corolla", "Aveo", "Jetta"],
    "año": [2015, 2020, 2017, 2018]
}

#Pasamos el diccionario dict a DataFrame dc
dc = pd.DataFrame(dict)#Hace una tabla

#Imprimimos el contenido del diccionario
print(dc)