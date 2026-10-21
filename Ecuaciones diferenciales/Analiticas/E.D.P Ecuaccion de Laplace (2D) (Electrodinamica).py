'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-MM-DD
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt

from numpy import pi, exp, sin
from matplotlib import rc 


# %% Definicion de constantes globales y espacions de memoria:

L = 1
V = 1

n = 10

# %% Definición de funciones:

def Serie(x, y, n):
        
    S = 0
    
    for k in range(1, n):
        s = (2*V/(pi*k))*((-1)**k)*sin(k*pi*x/L)*exp(-k*pi*y/L)
        S += s
        
    return S

def Potencial(x, y):
    
    Psi = V/L*x + Serie(x, y, n)
    
    return Psi


# %% Programa principal:

X = np.linspace(0, L, 100)
Y = np.linspace(0, 2*L, 100)

Psi = np.zeros([len(X), len(Y)])

for i in range(len(X)):
    for j in range(len(Y)):
        Psi[i, j] = Potencial(X[j], Y[i])

X, Y = np.meshgrid(X, Y)


# %% Imprimir los datos:

rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)    

Fig = plt.figure(figsize = (6, 10))    
Ax = Fig.add_subplot()

g = Ax.contourf(X, Y, Psi, cmap = 'Blues', levels = 20)
Ax.set_xlim(0, L)
Ax.set_ylim(0, 2*L)

Ax.set_xlabel('$x$', fontsize = 20)
Ax.set_ylabel('$y$', fontsize = 20)
Ax.set_title(r'$\Phi(x, y)$', fontsize = 20)

Fig.colorbar(g)
plt.show()


