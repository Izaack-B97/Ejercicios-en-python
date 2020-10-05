# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:50:37 2020

@author: Isaac Bustamante
"""

def calcularIndices(a,b):
    for i in range(len(a)):
        indices.append(float(a[i])/float(b[i]))
    return indices

altura = []#Array que iran las alturas
masa = []#Array que iran las masas 
indices = []#Array que iran los indices

x = input("Introduzca la altura 1:\n")
altura.append(x)
x = input("Introduzca la masa 1:\n")
masa.append(x)


x = input("Introduzca la altura 2:\n")
altura.append(x)
x = input("Introduzca la masa 2:\n")
masa.append(x)


x = input("Introduzca la altura 3:\n")
altura.append(x)
x = input("Introduzca la masa 3:\n")
masa.append(x)

calcularIndices(masa,altura)

paciente = 0
for i in indices:
    paciente = paciente + 1;
    print("El IMC del paciente " + str(paciente) + " es: " + str(i))
    #Validamos la categoria de peso en la que se encuentra
    if i < 18.5:
        print("BAJO PESO")
    elif i >= 18.5 and i <= 25:
        print("NORMAL")
    elif i >= 25 and i <= 30 :
        print("SOBREPESO")
    else:
        print("DEMACIADO OBESO")
        



