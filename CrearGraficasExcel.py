# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:51:08 2020

@author: DELL
"""

"""Crear un scrip donde graficas con los datos que tenemos en un excel"""

#import pandas as pd
#import matplotlib.pyplot as plt

#estados = pd.read_csv('C://Datos/estados.csv')
"""print('estas leyendo un excel')

#Declaramos los arrays correspondientes
array_estados = []
array_capitales = []
array_noEstados = []

#Iteramos los valores de cada columna y la agregamos a su correspondiente array
for i in estados['ESTADO']:
    array_estados.append(i)
for i in estados['CAPITAL']:
    array_capitales.append(i)
for i in estados['NUMESTADO']:
    array_noEstados.append(i)    


plt.plot(array_noEstados,array_estados)



#plt.plot(array_noEstados,array_capitales)
#plt.plot(array_noEstados,array_noEstados)

#Imprimimos los arrays
#print(array_estados)
#print(array_capitales)
#print(array_noEstados)

#print(estados)


e = 0
ss = 0
a = 0
o = 0
lista = estados['ESTADO']
for s in lista:
    if s.endswith("e"):
        e = e + 1 
    if s.endswith("s"):
        ss = ss + 1 
    if s.endswith("a"):
        a = a + 1 
    if s.endswith("o"):
        o = o + 1 
datos = [e,ss, a, o]
nombres = ['e','s','a', 'o']

plt.pie(datos, labels=nombres, autopct="%0.1f %%")
plt.show()"""


import pandas as pd 
import matplotlib.pyplot as plt
estados = pd.read_csv('C://Datos/estados.csv')

#lista = estados["c"]
#lista.sort()
c = 0
ss = 0
t = 0
lista = estados['ESTADO']
for s in lista:
    if s.startswith("C"):
        c = c + 1 
    if s.startswith("S"):
        ss = ss + 1 
    if s.startswith("T"):
        t = t + 1 
        
datos = [c,ss, t]
nombres = ['Letra c','Letra S', 'Letra T']

#Histograma
fig = plt.figure(u'Gráfica de barras') # Figure
ax = fig.add_subplot(111) # Axes
xx = range(len(datos))
ax.bar(xx, datos, width=0.8, align='center')
ax.set_xticks(xx)
ax.set_xticklabels(nombres)
plt.show()

#Grafica de pasteles
plt.pie(datos, labels=nombres, autopct="%0.1f %%")
plt.show()

















