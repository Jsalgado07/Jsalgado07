'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-MM-DD
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt

from numpy import arange, pi
from matplotlib import rc 


# %% Definicion de constantes globales y espacions de memoria:

L = 1
V = 1
    
Delta_t = 0.001
Delta_x = V*Delta_t

T_max = 10

T = arange(0, T_max+Delta_t, Delta_t)
X = arange(0,L+Delta_x, Delta_x)


# %% Definición de funciones:




# %% Programa principal:

A, B = np.meshgrid(T, X)
Psi = np.zeros(A.shape)
Psi.fill(0)

Psi[:, 0] = np.sin(pi*X)
for i in range(len(T)-1):
    for j in range(1, len(X)-1):
        if i == 0:
            Psi[j, i+1] = 1/2*(Psi[j+1, i] + Psi[j-1, i])
        else:
            Psi[j, i+1] = Psi[j+1, i] + Psi[j-1, i] - Psi[j, i-1]

                               

# %% Imprimir los datos:

rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)  

Fig = plt.figure(figsize= (8, 6))

plt.imshow(Psi, extent = (min(T), max(T), min(X), max(X)), 
           aspect = 5, origin = 'lower')

plt.title('Ecuacion de onda', size = 30)
plt.xlabel(r'$t$', size = 20)
plt.ylabel(r'$x$', size = 20)
plt.colorbar()

plt.show