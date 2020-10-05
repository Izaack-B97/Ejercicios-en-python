# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 18:07:25 2020

@author: ISAAC BUSTAMANTE
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("C://Datos/Airline Satisfaction Survey.csv", )

""" AÑOS EN EL QUE SE BRINDO MEJOR SERVICIO
anios = data['Year of First Flight'].unique()

years = sorted(anios)

#for i in data.loc[:100,'Year of First Flight']:
 #   print(i)
 
satisfacciones = [0,0,0,0,0,0,0,0,0,0]
 
for i in range(0,len(years)):
    for j in data.loc[:100,'Year of First Flight']:
        if(years[i] == j):
            satisfacciones[i] += 1
    

#datos = [media,mediana,desviacion_estandar,percentil]
#nombres = ['Media','Mediana','Desviacion Estandar','Percentiles']

fig = plt.figure(u'Gráfica de barras') # Figure
ax = fig.add_subplot(111) # Axes
xx = range(len(satisfacciones))
ax.bar(xx, satisfacciones, width=0.8, align='center')
ax.set_xticks(xx)
ax.set_xticklabels(years)
plt.show()

#print(satisfacciones)"""

""" EL ESTATUS DE LA AEROLINEA QUE TIENE MAS COMPRAS EN PESOS
compras_vuelos = [0,0,0,0]
airline_status = data['Airline Status'].unique()
print(airline_status)
#for i in range(0,len(airline_status)):
#print(data[{'Airline Status','Shopping Amount at Airport'}])
for j,rows in data.iterrows():
   if(rows['Airline Status'] == "Blue"):
       compras_vuelos[0] += rows['Shopping Amount at Airport']
   elif(rows['Airline Status'] == "Silver"):
       compras_vuelos[1] += rows['Shopping Amount at Airport']
   elif(rows['Airline Status'] == "Gold"):
       compras_vuelos[2] += rows['Shopping Amount at Airport']
   else:
       compras_vuelos[3] += rows['Shopping Amount at Airport']

print(compras_vuelos)
#Grafica de pasteles
plt.pie(compras_vuelos, labels=['Blue','Silver','Golden','Platinum'], autopct="%0.1f %%")
plt.show()
"""

#-----------------------------------------------


"""AEROLIONEA QUE MAS VIAJA
frecuencias_class = [0, 0, 0]
clases = data['Class'].unique()
print(clases)

for i in range(0,len(clases)):
    for index,row in data[0:100].iterrows():
        if(clases[i] == row['Class']):
            frecuencias_class[i] += 1

print(frecuencias_class)

fig = plt.figure(u'Gráfica de barras') # Figure
ax = fig.add_subplot(111) # Axes
xx = range(len(frecuencias_class))
ax.bar(xx, frecuencias_class, width=0.8, align='center')
ax.set_xticks(xx)
ax.set_xticklabels(clases)
plt.show()"""


#print(data.loc[:3,'Destination State'].unique())

arrayA = []
#arrayB = []
#arrayC = []
#a = 0

print(data.loc[:100, 'Destination State'].unique())

for i,row in data[0:100].iterrows():
    if row['Destination State'] == "Texas":
        arrayA.append(row['No of Flights p.a.'])

print(arrayA)
#print(arrayB)
#print(arrayC)
array_numpy = np.array(arrayA)

plt.plot(array_numpy, marker='*', color='m', label = 'Vuelos a Texas', linestyle = '-.')
plt.title("Comportamiento del No. de Vuelos por Aerolinea")
plt.ylabel("No. Vuelos para Texas")

plt.legend()#Mostarmos el label



























