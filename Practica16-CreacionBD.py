# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:33:32 2020

@author: Isaac Bustamante

Objetivo: Aprender a crear bases de datos, crear tablas e insertar registros usando MySQL en Python.

"""
# Importamos MySQL connector
import mysql.connector

mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "myseconddatabase"
        )

# Creamos el cursor para poder interactuar con MySQL
mycursor = mydb.cursor()

# Crearemos nuestra primera base de datos
#mycursor.execute("CREATE DATABASE myseconddatabase")

# Indicamos mostrar las bases de datos existentes
#mycursor.execute("SHOW DATABASES")

# Mostramos las bd existentes
#for x in mycursor:
#    print(x)

# Crearemos la tabla llamada autos
#mycursor.execute("CREATE TABLE autos (Marca_Modelo VARCHAR(255), Disponibilidad INT(4), Precio_USD INT(8))")

#Crearemos la llave primaria en la tabla autos
#mycursor.execute("ALTER TABLE autos ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# Declararemos la variable donde se encontraran los valores
"""sql = [
       "INSERT INTO autos  VALUES ('Audi A8', 2, 45000, 1)",
       "INSERT INTO autos  VALUES ('Audi TT coupe', 3, 40000, 2)",
       "INSERT INTO autos  VALUES ('Audi Q7', 4, 35000, 3)",
       "INSERT INTO autos  VALUES ('Audi R8', 2, 30000, 4)",
       "INSERT INTO autos  VALUES ('BMW X6 xDrive 35i', 3, 25000, 5)",
       "INSERT INTO autos  VALUES ('BMW x5 48i', 6, 40000, 6)",
       "INSERT INTO autos  VALUES ('BMW x5 30d', 2, 35000, 7)",
       "INSERT INTO autos  VALUES ('BMW x5 xDrive 25i', 5, 30000, 8)",
       "INSERT INTO autos  VALUES ('BMW x5 30i', 3, 25000, 9)",
       "INSERT INTO autos  VALUES ('BMW x1 xDrive 20d', 5, 40000, 10)",
       "INSERT INTO autos  VALUES ('BMW x1 sDrive 20d', 6, 35000, 11)",
       "INSERT INTO autos  VALUES ('BMW 750i', 2, 30000, 12)",
       ]

# Ingresamos los valores a la tabla
for i in range(len(sql)):
    mycursor.execute(sql[i]);"""
    
# Mostramos el contenido de la tabla autos
mycursor.execute("SELECT * FROM autos")
print(mycursor)
for i in mycursor:
    print(i)