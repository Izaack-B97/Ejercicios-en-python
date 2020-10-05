# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:41:35 2020

@author: ISAAC BUSTAMANTE

19.	Como actividades de esta práctica, se deberá realizar lo siguiente:
•	Generar el macro y archivo CSV (limpio). 
•	Crear un script en Python que lea el archivo CSV, generando gráficas, conteos, etc.; 
se deberá generar un reporte en Word con texto explicando cada gráfica y resultado.

"""
# Importamos las librerias correspodientes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Leemos el archivo csv
df = pd.read_csv("C://Datos/DATOS_ESCUELAS.csv")

"""  START GRAFICAS   """

# CHAMBA PARA LOS TURNOS
print('\n************************** SECTOR DOMINANTE (PUBLICA, PRIVADA) **********************************\n')
turnos = df['Turno'].unique()
contador_turnos = np.zeros(len(turnos), dtype=int)

for i in range(0, len(turnos)):
    for j in df['Turno']:
        if(turnos[i] == j):
            contador_turnos[i] += 1
    # Imprimimos los turnos con su distribucion
    print("Turno " + str(turnos[i]) + " -> Distribucion: " + str(contador_turnos[i]))
    
#Grafica de pasteles
plt.title("DOSTRIBUCION DE TURNOS")
plt.pie(contador_turnos, labels=turnos, autopct="%0.1f %%")
plt.show()


# CHAMBA PARA LA GRAFICA DEL SECTOR DOMINATE
print('\n************************** SECTOR DOMINANTE (PUBLICA, PRIVADA) **********************************\n')
sost = df['Sost.'].unique()
contador_sost = [0, 0]

for i in range(0, len(sost)):
    for j in df['Sost.']:
        if(sost[i] == j):
            contador_sost[i] += 1
            
print("Sost. " + str(sost[0]) + " -> PREDOMINACION: " + str(contador_sost[0]))
print("Sost. " + str(sost[0]) + " -> PREDOMINACION: " + str(contador_sost[1]))

#Grafica de pasteles
plt.title("SECTOR PREDOMINANTE EN LAS ESCUELAS")
plt.pie(contador_sost, labels=sost, autopct="%0.1f %%")
plt.show()

# CHAMBA PARA EL NIVEL ESCOLAR QUE TIENE MAS PLANTELES
print('************************** NIVELES ESCOLARES CON MAS ESCUELAS **********************************\n')
niveles_escolares = df['Nivel escolar'].unique()
count_nivel_escolar = np.zeros(len(niveles_escolares) ,dtype=int)

for i in range(0, len(niveles_escolares)):
    for nivel_escolar in df['Nivel escolar']:
        if(niveles_escolares[i] == nivel_escolar):
            count_nivel_escolar[i] += 1
    # Imprimimos el nivel escolar con el total de planteles
    print("Nivel escolar: " + str(niveles_escolares[i]) + " - Planteles: " + str(count_nivel_escolar[i]))


# Grafica de barras con rotulos
plt.bar(range(len(count_nivel_escolar)), count_nivel_escolar, edgecolor = 'm', color = 'b')
# Indicamos los rotulos del eje x con propieades
plt.xticks(range(len(count_nivel_escolar)), niveles_escolares, rotation = -90)
# Indicamos el titulo del grafico
plt.title('DISTRINUCION DE PLANTELES SEGUN EL NIVEL ESCOLAR')
# Indicamos los valores del eje y 
plt.ylim(min(count_nivel_escolar)-1, max(count_nivel_escolar)+1)
# Rotulos de x & y
plt.xlabel("Nivel escolar")
plt.ylabel("No. Plantceles") 
plt.show()

# CHAMBA PARA LA DISTRIBUCION DE ESCUELAS POR LOCALIDADES
print('************************** DISTRIBUCION DE PLANTELES POR MUNICIPIO/EJIDO **********************************\n')
localidades = df['Localidad'].unique()
logitud = len(localidades)
frecuencias_localidades = np.zeros(logitud, dtype=int)

for i in range(0, logitud):
    for localidad in df['Localidad']:
        if(localidades[i] == localidad):
            frecuencias_localidades[i] += 1

print("-------------------- FRECUENCIAS POR LOCALIDAD ------------------------\n")
json_localidades_frecuencias = { 'Localidades': localidades, 'Distribucion':  frecuencias_localidades}
df_localidades_frecuencias = pd.DataFrame(json_localidades_frecuencias)
print(df_localidades_frecuencias)

array_numpy = np.array(frecuencias_localidades) # Convertimos las frecuencias en un arreglo numpy

plt.figure(figsize=(12,8)) # Primero definimos el tamaño del grafico

# Despues ya hacemos toda la chamba de la grafica
plt.plot(array_numpy, marker = '*', color = 'b', label = 'Distribucion de planteles', linestyle = '-')
plt.title("DISTRIBUCION DE PLANTELES POR MUNICIPIO")
plt.xlabel("Municipios")
plt.ylabel("No. Planteles")

plt.legend()

indice = np.arange(len(localidades))
plt.xticks(indice, localidades, rotation = -90)
#plt.yticks(0,110,10)








