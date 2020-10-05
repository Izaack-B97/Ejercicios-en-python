# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:22:13 2020

@author: Isaac Bustamante
@correo: izaack.97@gmail.com

17.	Crearemos un script que cree una base de datos, una tabla con 4 columnas diferentes,  
ingresaremos 10 registros y mostraremos los registros ingresados. (Todo se debe de realizar en una sola corrida).

"""
# Importamos MySQL
import mysql.connector as mysql
# Importamos pandas
import pandas.io.sql as pd
# Importamos la matplot
import matplotlib.pyplot as plt

mydb = mysql.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            #database = "maranatha_music"
        )

#Creamos el cursor
mycursor = mydb.cursor()

#Eliminamos la base de datos si es que existe
mycursor.execute("DROP DATABASE IF EXISTS maranatha_music")

# Creamos la base de datos
mycursor.execute("CREATE DATABASE maranatha_music")

# Seleccionamos la base de datos
mycursor.execute("USE maranatha_music")

# Query de creacion de la tabla
create_table = "CREATE TABLE instrumentos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(20), modelo VARCHAR(50), precio INT(5), unidades_vendidas INT)" 

# Creamos la tabla 
mycursor.execute(create_table)

# Insertaremos algunos registros
sql = [
       "INSERT INTO instrumentos VALUES (1,'Guitarra', 'Fender XSD45', 1897, 20)",
       "INSERT INTO instrumentos VALUES (2,'Piano', 'Metrico Plat 4450', 30000, 14)",
       "INSERT INTO instrumentos VALUES (3,'Matracas', 'Tambiser Grises 45ID', 1250, 40)",
       "INSERT INTO instrumentos VALUES (4,'Flauta', 'Blanca Firzex 4895', 2600, 30)",
       "INSERT INTO instrumentos VALUES (5,'Bateria', 'Black Edison 78D', 45660, 45)",
       "INSERT INTO instrumentos VALUES (6,'Marimbas', 'Chapanecas 458D', 6550, 90)",
       "INSERT INTO instrumentos VALUES (7,'Ukelele', 'Tamaulipeño 45FG', 4560, 100)",
       "INSERT INTO instrumentos VALUES (8,'Bajo', 'Fender FF5', 4892, 150)",
       "INSERT INTO instrumentos VALUES (9,'Acordion', 'RestarD 45', 36600, 15)",
       "INSERT INTO instrumentos VALUES (10,'Guitarra Electrica', 'Yamaha Negra XSD45', 48990, 80)",
       ]

for i in sql:
    mycursor.execute(i)

# Mostramos los registros de la tabla
mycursor.execute("SELECT * FROM instrumentos ORDER BY modelo")
for i in mycursor:
    print(i)

# Hacemos la chamba para la grafica
query = "SELECT id, nombre, unidades_vendidas FROM instrumentos "
df = pd.read_sql(query, con = mydb) # Convierte en un dataframe una consulta en mysql
print(df)


""" *** GRAFICA DE BARRAS CON ROTULOS INCLINADOS *** """
# Dibujamos el grafico
plt.bar(range(10), df['unidades_vendidas'], edgecolor = 'red', color = 'm')

# Indicamos los rotulos del eje x con propieades
plt.xticks(range(10), df['nombre'], rotation = 90)

# Indicamos el titulo del grafico
plt.title('Ganancias segun la empresa')

# Indicamos los valores del eje y 
plt.ylim(min(df['unidades_vendidas'])-1, max(df['unidades_vendidas'])+1)

# Rotulos de x & y
plt.xlabel("Intrumentos")
plt.ylabel("Unidades") 

#Mostramos el grafico
plt.show()

"""# Actualizaremos las unidades vendidas del bajo
mycursor.execute("UPDATE instrumentos SET unidades_vendidas=10 WHERE id=8")

print(" -----------------------  *** UPDATED ***  ----------------------------------- ")

# Hacemos la chamba para la grafica
query = "SELECT id, nombre, unidades_vendidas FROM instrumentos"
df = pd.read_sql(query, con = mydb) # Convierte en un dataframe una consulta en mysql
print(df)
"""

""" *** GRAFICA DE BARRAS CON ROTULOS INCLINADOS *** """
"""# Dibujamos el grafico
plt.bar(range(10), df['unidades_vendidas'], edgecolor = 'red', color = 'm')

# Indicamos los rotulos del eje x con propieades
plt.xticks(range(10), df['nombre'], rotation = 90)

# Indicamos el titulo del grafico
plt.title('Ganancias segun la empresa')

# Indicamos los valores del eje y 
plt.ylim(min(df['unidades_vendidas'])-1, max(df['unidades_vendidas'])+1)

# Rotulos de x & y
plt.xlabel("Intrumentos")
plt.ylabel("Unidades") 

#Mostramos el grafico
plt.show()

# Cerramos la conexion a la base de datos
mydb.close()"""

# Aplicamos seleccionar unos cuantos campos, un WHERE 

print("*******************************************************")
query = "SELECT nombre, modelo, precio FROM instrumentos WHERE modelo LIKE " 
query += "'%fender%' ORDER BY nombre ASC"

mycursor.execute(query)
print(query)
for i in mycursor:
    print(i)

