# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 18:21:56 2020

@author: DELL
"""

#Crearemos un bucle while
"""i = 0
while i <= 50:
    print(i)
    i = 5 + i
"""

#Crea un scrip que calcule cualquier tabla 1-10, dependiendo del numero que ingrese
#el usuario con el ciclo for

"""x = int(input("¿Que tabla quiere multiplicar?"))

for i in range(1,11):
    print(str(x) + " x " + str(i) + " = "+ str((x*i)))
"""
#Crea un scrip que imprima la suma de todos los numeros pares que van del 1-100
"""suma = 0
for i in range(1,101):
    if(i % 2 == 0):
        suma = suma + i
        
print("Total de numeros pares: ",suma)
"""
#Creamos un script que imprima todos los numeros inferiores a un numero que el usuario ingrese  y este lo haremos con el while 
x = int(input("Dame un numero: \n"))

while(x >= 1):
    x -= 1
    print('----')
    print(x)