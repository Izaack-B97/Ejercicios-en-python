# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:29:35 2020

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
"""
indice = np.arange(12)
plt.xticks(indice, ("ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC")) 
plt.yticks(np.array(0,110,10))
plt.show()
"""
plt.show()
