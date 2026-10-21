'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-04-12
'''


# %% Importación de librerías:

import matplotlib.pyplot as plt
from numpy import arange


# %% Definicion de constantes globales y espacions de memoria:

h = 0.1
f = lambda x: x**4/4 + x**3/2 + x**2*5/4 + x + 1 


# %% Definición de funciones:

def Ec(x, y):
    dy = (1 + 2*x)*(y**0.5)    
    return dy


def RungeKutta2(x0, xf, h, y0):
    
    X = arange(x0, xf, h)
    Y = [y0]
    
    for i in range(len(X)-1):       
        k1 = Ec(X[i], Y[i])
        k2 = Ec(X[i] + h/2, Y[i] + h*k1/2)
        y = Y[i] + k2*h
        Y  += [y]    
    return X, Y


# %% Programa principal:

X, Y = RungeKutta2(0, 5, h, 1)


# %% Imprimir los datos:

Fig = plt.figure(figsize = (10, 6))
Ax  = Fig.add_subplot()

Ax.plot(X, Y, 'o-', label=f'Metodo del paso medio $h={h}$')
Ax.plot(X, f(X), '*-', label = 'Solucion analitica')

plt.legend()
plt.grid()
plt.show()