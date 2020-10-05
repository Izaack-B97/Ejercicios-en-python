# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:18:22 2020

@author: Mike

crear script que grafique algo basado en las categorias de los pasajeros(blue platinum)
y checar los niveles de insatisfaccion basado en los retrasos de salida del vuelo
+ rangos de edades
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('C:/Datos/Airline Satisfaction Survey.csv', nrows = 100)

sampleS = df["Satisfaction"]
sampleAS = df["Airline Status"]
sampleAD = df["Arrival Delay greater 5 Mins"]
sampleA = df["Age"]

uniqS = list(set(sampleS))
uniqAS = list(set(sampleAS))
totalFS = np.zeros((2,len(uniqAS)))
totalS = np.zeros(8)

print(uniqS)

for i in range(0,len(sampleS)):
    if sampleAS[i] == "Platinum":
        if sampleAD[i] == "yes":
            totalFS[0][0] += 1
            totalS[0] += sampleS[i]
        else:
            totalFS[1][0] += 1
            totalS[1] += sampleS[i]
    if sampleAS[i] == "Gold":
        if sampleAD[i] == "yes":
            totalFS[0][1] += 1
            totalS[2] += sampleS[i]
        else:
            totalFS[1][1] += 1
            totalS[3] += sampleS[i]
    if sampleAS[i] == "Silver":
        if sampleAD[i] == "yes":
            totalFS[0][2] += 1
            totalS[4] += sampleS[i]
        else:
            totalFS[1][2] += 1
            totalS[5] += sampleS[i]
    if sampleAS[i] == "Blue":
        if sampleAD[i] == "yes":
            totalFS[0][3] += 1
            totalS[6] += sampleS[i]
        else:
            totalFS[1][3] += 1
            totalS[7] += sampleS[i]
            
totalFS[0][0] = totalS[0]/totalFS[0][0]
totalFS[1][0] = totalS[1]/totalFS[1][0]
totalFS[0][1] = totalS[2]/totalFS[0][1]
totalFS[1][1] = totalS[3]/totalFS[1][1]
totalFS[0][2] = totalS[4]/totalFS[0][2]
totalFS[1][2] = totalS[5]/totalFS[1][2]
totalFS[0][3] = totalS[6]/totalFS[0][3]
totalFS[1][3] = totalS[7]/totalFS[1][3]

x = np.arange(4)

plt.bar(x + 0.00,totalFS[0], color = "k",width = .25)

plt.bar(x + 0.25,totalFS[1], color = "b",width = .25)


plt.xticks(x+.12, ["Platinum","Gold","Silver","Blue"])

plt.ylabel("Satifaccion promedio")

plt.xlabel("Con/Sin Retraso por Categoria")

plt.title("Satifaccion promedio del vuelo por clases")