# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 13:38:39 2020

@author: Isaac Bustamante
"""
# importtamos mysql
import mysql.connector

mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "myseconddatabase" 
        )

# Creamos  el cursor para interactuar con mysql
cursor = mydb.cursor()

# Seleccionamos toda la tabla de autos
#cursor.execute("SELECT * FROM autos WHERE disponibilidad = 2");

# Seleccionamos solo los registros que tengan ala palabra audi
#cursor.execute("SELECT * FROM autos WHERE Marca_Modelo LIKE '%Audi%'");

# Seleccionamos todos los registros y los ordenamos por Marca_Modelo
cursor.execute("SELECT * FROM autos ORDER BY Marca_Modelo DESC")

# Usamos el metodo fetchAll
myresult = cursor.fetchall(); # Nos regresa todos los registros

# Usamos el metodo fetcone() -> Solo nos devolvera el primer registro
#myresult = cursor.fetchone()

# Mostramos el contenido de myresult
for x in myresult:
   print(x)
#print(myresult)