'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-05-04
'''


# %% Importación de librerías:
    
import numpy as np
import matplotlib.pyplot as plt

from numpy import zeros
from matplotlib import rc 


# %% Definicion de constantes globales y espacions de memoria:

X_len = 100
Y_len = 100

Psi = zeros([X_len, Y_len])

T_left = 1
T_righ = 0 
T_bottom = 0
T_top = 0    

n = int(1e4)


# %% Definición de funciones:

def Laplace(Psi):
    
    for i in range(1, X_len-1):
        for j in range(1, Y_len-1):
            Psi[i, j] = (1/4)*(Psi[i+1, j] + Psi[i-1, j] + 
                               Psi[i, j+1] + Psi[i, j-1])
        
    return Psi


# %% Programa principal:

Psi[0, :].fill(T_top) 
Psi[-1, :].fill(T_bottom)
Psi[:, 0].fill(T_righ)
Psi[:, -1].fill(T_left)

for i in range(n):
    Psi = Laplace(Psi)

X = np.linspace(0, 1, X_len)
Y = np.linspace(0, 100, Y_len)

X, Y = np.meshgrid(X, Y)

# %% Imprimir los datos:

rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)    

Fig = plt.figure(figsize = (5, 10))    
Ax = Fig.add_subplot()

Ax.contourf(X, Y , Psi, cmap = 'Blues')
Ax.set_xlim(0, 1)
Ax.set_ylim(0, 10)

Ax.set_xlabel('$x$', fontsize = 20)
Ax.set_ylabel('$y$', fontsize = 20)
Ax.set_title(r'$\Psi(x, y)$', fontsize = 20)


plt.show()
