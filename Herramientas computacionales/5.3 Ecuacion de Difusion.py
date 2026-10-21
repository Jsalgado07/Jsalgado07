'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-05-05
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt

from numpy import arange
from matplotlib import rc 

# %% Definicion de constantes globales y espacions de memoria:

Delta_x  = 0.01
Delta_t  = Delta_x**2 

X = arange(-1, 1+Delta_x, Delta_x)
T = arange(0, 0.1+Delta_t, Delta_t)

Psi = np.zeros([len(X), len(T)])

# %% Definición de funciones:

len_T = len(T)


# %% Programa principal:

m = int((len(X)-1)/2)
Psi[m][0] = 1/2
Psi[m+1][0] = 1/4
Psi[m-1][0] = 1/4

for j in range(0, len(T)-1):
    for i in range(1, len(X)-1):
        Psi[i][j+1] = 0.5*(Psi[i+1][j] + Psi[i-1][j]) 
    

# %% Imprimir los datos:

rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)   


plt.imshow(Psi, extent = (min(T), max(T), min(X), max(X)), aspect = 0.02)
plt.xlabel(r'$Tiempo$')
plt.ylabel(r'$Posicion$')
plt.title(r'Solución a la ecuación de difusión', fontsize = 15)
plt.colorbar()
plt.show()






