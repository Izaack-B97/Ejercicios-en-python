# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 18:34:20 2020

@author: Isaac Bustamante
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mat = np.arange(0,100).reshape(10,10)#Se llena un array con 100 numeros,y el 
#reshape redimensiona un array sin alterar sus valores

print(mat)

plt.imshow(mat, cmap="RdYlGn")#Dibuja un digrama de densidades
