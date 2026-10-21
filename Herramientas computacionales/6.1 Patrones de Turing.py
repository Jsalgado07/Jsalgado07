'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-05-21
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rc


# %% Definicion de constantes globales y espacions de memoria:

a  = 0.00028
b  = 0.005
τ  = 0.1
κ  = -0.005
h  = 0.02
dt = 0.001

Lx = 1
Ly = 1

X = np.arange(0, Lx + h, h)
Y = np.arange(0, Ly + h, h)


# %% Definición de funciones:

def Soluciones(N):

    φ = np.random.rand(len(X), len(Y)) 
    ψ = np.random.rand(len(X), len(Y))    

    for n in range(N):
        for i in range(1, len(X)-1):
            for j in range(1, len(Y)-1):
                
                L_φ = ((φ[i+1, j] + φ[i-1, j] + φ[i, j+1] + φ[i, j-1] - 
                        4*φ[i, j])/(h**2))
                
                φ[i, j] = φ[i, j] + dt*(a*L_φ + φ[i,j] - φ[i,j]**3 - 
                                        ψ[i, j] + κ)
                
                L_ψ = ((ψ[i+1, j] + ψ[i-1, j] + ψ[i, j+1] + ψ[i, j-1] - 
                        4*ψ[i, j])/(h**2))
                
                ψ[i, j] = ψ[i, j] + dt/τ*(b*L_ψ + φ[i, j] - ψ[i, j])

    return φ

    
# %% Imprimir los datos:

rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)  

for k in range(0, 12, 2):

    N = int(k/dt)
    
    φ = Soluciones(N)
    
    Fig = plt.figure(figsize= (8, 6))
    
    g = plt.contourf(X, Y, φ, levels = 100, cmap = 'magma')
    
    plt.title(f'Patrones de Turing t = {k}s', size = 30)
    plt.xlabel(r'$x$', size = 20)
    plt.ylabel(r'$y$', size = 20)
    Fig.colorbar(g)
    
    plt.show()







