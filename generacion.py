# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:04:06 2020

@author: DELL
"""

print("Introduce el año en que naciste:\n")
anio = int(input())

if(anio <= 2000 and anio >= 1990):
    print("Eres generacion z")
elif (anio < 1990 and anio >= 1980):
    print("Eres generacion millenials")
elif (anio < 1980 and anio >= 1960):
    print("Eres generacion x")
elif (anio < 1960 and anio >= 1940):
    print("Eres generacion baby womers")
elif (anio < 1940 and anio >= 1920):
    print("Eres generacion generacion silenciosa")