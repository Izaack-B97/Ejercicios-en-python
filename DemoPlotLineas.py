# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:14:20 2020

@author: martin.espinozas
"""

import matplotlib.pyplot as plt 
import numpy as np

ventas = [28,22,23,25,20,45,47,48,50,42,37,32]
vnts = np.array(ventas)

plt.plot(vnts)
plt.title("Ventas Auto 2000")
plt.xlabel("Meses")
plt.ylabel("Ventas(Promedio)")

plt.ioff()
ventas2019 = [20,22,23,24,28,32,24,26,29,42,45,47]
vnts19 = np.array(ventas2019)
plt.ion()
plt.plot(vnts19, label = 2019)
plt.legend()
plt.show()