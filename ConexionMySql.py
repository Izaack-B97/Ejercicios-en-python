# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:22:25 2020

@author: DELL
"""
# Importamos MySQL Connector
import mysql.connector

# Creamos la conexion
mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = ""
        )

# Imprimimos el estado de la conexion
print(mydb)

