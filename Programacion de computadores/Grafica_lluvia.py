# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:29:51 2020

@author: Juan Diego
"""

#Importacion de modulos
import numpy as np
from matplotlib import pyplot as plt


#Generador de datos para los graficos
lluvias_mensuales = np.random.randint(0, 600, size = [12])
Meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
mn =range(len(Meses))


#Crear grafico
plt.plot(pm_2000, label = 'Año 2000')
plt.xlabel('Mes')
plt.ylabel('Presipitacion (mm)')


