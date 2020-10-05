# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 18:18:47 2020

@author: DELL
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%matplotlib inline

x = np.arange(0,10)
print(x)

y = x**2#Eleva al cuadrado todo el array
print(y)
plt.plot(x,y)#Grafica dos arrays (Hace una grafica jupiter)