# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:06:10 2020

@author: DELL
"""

print("Dame tu calificacion")
a = int(input())

if(a >= 90 and a <= 100):
    print("Tu calificacion es buena")
elif(a < 90 and a >= 70):
    print("Tu calificacion es regular")
elif (a < 70):
    print("Tu calificacion es mala")
    
    