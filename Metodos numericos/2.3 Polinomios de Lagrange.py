'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2021-11-08

A partir de un conjunto de datos, encontrar y graficar un polinomio que 
conecte estos mediante polinomios de Lagrange.

'''


# %% Importación de librerías:

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


# %% Definicion de constantes globales y espacions de memoria:

X = [1, 2, 3, 4, 6]
Y = [5, 7, 9, 3, 0]
m = len(X)

x = sp.symbols('x')


# %% Definición de funciones:

def Polinomio_Lagrange(X, Y):

    y = 0
    for j in range(m):
        P = 1
        for i in range(m):
            if i != j:
                P *= (x-X[i])/(X[j]-X[i])
        y += P*Y[j]
    
    y = sp.expand(y)
    f = sp.lambdify(x, y)

    return f, y


# %% Programa principal:

f, y = Polinomio_Lagrange(X, Y)


# %% Imprimir los datos:

print('El polinomio de Lagrange para el conjunto de puntos es:\n y = ' , y)    

X_g = np.linspace(min(X), max(X), 1000)
Y_g = f(X_g)

plt.plot(X_g, Y_g)
plt.plot(X, Y, '.k',)
for i in range(m):
    plt.annotate(f'({X[i]}, {Y[i]})', (X[i]+0.1, Y[i]+0.1))
plt.show()

