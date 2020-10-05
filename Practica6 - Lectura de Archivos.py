# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 18:26:45 2020

@author: DELL
"""

#Abrimos el archivo 
x = open("C://Datos/Prueba.txt","r")

#Imprimos el contenido del archivo
#print(x.read(6))#El metodo read devuelve todo el texto dentro del archivo(Puede recibir como parametro la ongitud de caracteres que desea)
#print(x.readline())#Nos devuelve una sola linea

#for i in x:
 #   print(i)#Asi podemos recorrer todas las lineas del archivo

#x.close()#Es una buena practica cerrar el archivo cuando se termina con el

#Crear el archivo
#a = open("C://Datos/ArchivoCreado.txt","a")#Creamos el archivo

#a = open("C://Datos/ArchivoCreado.txt","w")#Sobreescribimos
#Indicamos que escribir
#a.write("Esta linea se sobreescribio")

#a.close()

import os

#Eliminamos un archivo
#os.remove("C://Datos/ArchivoCreado.txt")

#Validamos si existe el archivo y lo eliminamos
#if os.path.exists("C://Datos/Prueba.txt"):
 #   os.remove("C://Datos/Prueba.txt")
#else:
 #   print("El archivo no existe")
    
#Crearemos un script que cree un archivo llamado tablas de multiplicar y escribira en dicho archivo las tablas del 1-10 
#
a = ""
if os.path.exists("C://Datos/TablasDeMultiplicar.txt"):
    print("Ya existe")
else: 
    a = open("C://Datos/TablasDeMultiplicar.txt","a")
    

texto = ""

for i in range(1,11):
    for j in range(1,11):
        texto = texto + str(i) + " x " + str(j) + " = " + str(i*j) +  "\n" 
        if(j == 10):
            texto = texto + "\n-----------------------------  \n"
        
b = open("C://Datos/TablasDeMultiplicar.txt","w")
print(texto)
b.write(texto)
print('Paso escribir en el archivo')
