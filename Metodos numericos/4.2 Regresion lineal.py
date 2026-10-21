'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2022-01-24
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt


# %% Definicion de constantes globales y espacions de memoria:

X = [0, 0.13, 0.25, 0.38, 0.51, 0.64, 0.76, 0.89, 1.02, 1.14, 1.27, 1.4,
      1.52, 1.65, 1.78, 1.91, 2.03, 2.16, 2.29, 2.41, 2.54]
Y = [0, 27.27, 63.64, 90.91, 118.18, 136.36, 163.64, 172.73, 200, 218.18,
      236.36, 245.45, 263.64, 290.91, 300, 318.18, 327.27, 345.45, 354.55, 
      390.91, 400]


T = [3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000,
     5200, 5400, 5600, 5800, 6000]

E = [4.6,5.9, 7.6, 9.5 ,11.8, 14.5, 17.6, 21.3, 25.4, 30.1, 35.4, 41.5, 48.2,
     55.8, 64.2, 73.5]



n = len(E)

Mi = []




# %% Programa principal:

for k in range(n-1):

    m = (E[k] - E[k+1])/(T[k] - T[k+1])  
    Mi.append(m)
    
M = np.mean(Mi)
B = np.mean(Y) - M*np.mean(X)


# %% Imprimir los datos:

print('La ecuacion lineal por el metodo de minimos cuadrados es: Y = ', 
      M,'x + ',B )


# %% Graficar los datos:



