# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 08:55:08 2020

@author: Isaac Bustamante
"""
# Importamos las librerias necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector

# Hacemos la conexion con la bd
mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "ntic"
        )

query = df = "" # Usaremos estas variables para reusarlas una y otra vez

#query = "SELECT Grupo, Periodo, AVG(ORD) as Promedio FROM calificaciones "
#query += "GROUP BY Grupo HAVING AVG(ORD) >= 60 ORDER BY Periodo DESC LIMIT 20;"
#df = pd.read_sql(query, con = mydb)
#print(df)

# Comportamiento de las bajas segun el grupo en la asignatura de NTIC

# Seleccionamos los grupos con sus bajas totales solo aquellas que las han tenido
query = "SELECT Grupo, SUM(Bajas) as BajasTotales FROM calificaciones WHERE Bajas > 0 GROUP BY Grupo;"
df = pd.read_sql(query, con = mydb)
#print(df)

bajas = []
grupos = []

for x,row in df.iterrows():
    #if(row['BajasTotales'] > 1):
    bajas.append(int(row['BajasTotales']))
    grupos.append(row['Grupo'])
        
#print(bajas)
#print(grupos)

array_numpy = np.array(bajas) # Convertimos las bajas en un arreglo numpy

plt.figure(figsize=(12,8)) # Primero definimos el tamaño del grafico

# Despues ya hacemos toda la chamba de la grafica
plt.plot(array_numpy, marker = '*', color = 'b', label = 'Comportamiento de bajas en los grupos', linestyle = '-')
plt.title("Bajas por Grupo en la Asignatura de NTIC")
plt.xlabel("Grupos")
plt.ylabel("No. Bajas")

plt.legend()

indice = np.arange(len(grupos))
plt.xticks(indice, grupos, rotation = -90)
#plt.yticks(0,110,10)


#--------------------------------------------------------------------------------------------------

# Revisamos cual fue el periodo que tuvo mas inscriptos en la asignatura de NTIC


"""# Seleccionamos los ultimos 10 periodos y sumamos sus numeros de inscritos en dichos periodos
query = "SELECT Periodo, SUM(Insc) as Inscriptos FROM calificaciones GROUP BY Periodo ORDER BY Periodo DESC LIMIT 10;"
df = pd.read_sql(query, con = mydb)
print(df)

# *** GRAFICA DE BARRAS CON ROTULOS INCLINADOS *** 

#Dibujamos el grafico
plt.bar(range(len(df['Inscriptos'])), df['Inscriptos'], edgecolor = 'black', color = 'b')

#Indicamos los rotulos del eje x con propieades
plt.xticks(range(len(df['Periodo'])), df['Periodo'], rotation = 60)

#Indicamos el titulo del grafico
plt.title('No. de Inscritos de los ultimos 10 periodos')

#Indicamos los valores del eje y 
plt.ylim(min(df['Inscriptos'])-1, max(df['Inscriptos'])+1)
plt.ylabel("No. Alumnos")
plt.xlabel("Periodo")

#Mostramos el grafico
plt.show()


#---------------------------------------------------------------------------------------------------

# COMPORTAMIENTO DE LOS APROBADOS Y REPROBADOS EN LOS ULTIMOS 10 PERIODOS(5 AÑOS)

# Hacemos la chamba para los aprobados
print("************ APROBADOS ************")

query = "SELECT Periodo, COUNT(Status) AS TOTAL FROM calificaciones WHERE Status='A' "
query += "GROUP BY Periodo ORDER BY Periodo DESC LIMIT 10" # Jalamos los ultimos 10 registros con sus periodos mas recientes

df = pd.read_sql(query, con = mydb)
df_aprobados = df.sort_values(by = 'Periodo', ascending = True)
print(df_aprobados)
aprobados = np.array(df_aprobados['TOTAL'])
#print(aprobados)

# Dbujamos la grafica
plt.plot(aprobados)
plt.title("COMPORTAMIENTO DE EVALUACIONES DEL PERIODO 2192 - 2141")
plt.xlabel("Periodo")
plt.ylabel("Indice de Aprobados/Reprobados")

# Hacemos la chamba de los reporbados
print("************ REPROBADOS ************")

query = "SELECT Periodo, COUNT(Status) AS TOTAL FROM calificaciones WHERE Status='R' "
query += "GROUP BY Periodo ORDER BY Periodo DESC LIMIT 10" # Jalamos los ultimos 10 registros con sus periodos mas recientes

df = pd.read_sql(query, con = mydb)
df_reprobados = df.sort_values(by = 'Periodo', ascending = False)
print(df_reprobados)

plt.ioff() # Desactivamos la forma dinamica del grafico
reprobados = np.array(df_reprobados['TOTAL'])
#print(reprobados)

periodos = df['Periodo'].sort_values(ascending = True) # Ordenamos los periodos de forma ascendente
#print(periodos)

# Terminamos la chamba del grafico
plt.ion()
plt.plot(aprobados, label = 'Aprobados')
plt.plot(reprobados, label = 'Reprobados')
plt.xticks(range(len(periodos)), periodos)
plt.legend()
plt.show()
"""