'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2021-19-12
'''

# %% Importación de librerías:

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


# %% Definicion de constantes globales y espacions de memoria:

X = [4.5, 3.0, 7.0, 9.0]
Y = [1.0, 2.5, 2.5, 0.5]
m = len(X)


# %% Definición de funciones:

def Trazadores_lineales(X_g, X, Y):
    
    x = sp.symbols('x')

    X = np.array(X, dtype = float)
    Y = np.array(Y, dtype = float)
    P = np.array([X, Y]).T
    P = P[np.lexsort(np.fliplr(P).T)]
    X = P[:, 0]
    Y = P[:, 1]
    
    M = (Y[1:]-Y[:-1])/(X[1:]-X[:-1])
    F = Y[:-1] + M*(x-X[:-1])        

    y = 0
    for i in range(m-1):
        F_i   = sp.lambdify(x, F[i])
        if i == 0:
            L_inf = X[i] <= X_g 
        else:
            L_inf = X[i] < X_g
        L_sup = X_g  <= X[i+1]
        y += L_inf*L_sup*F_i(X_g) 

    return y


# %% Programa principal:

X_g = np.linspace(min(X), max(X), 1000)
Y_g = Trazadores_lineales(X_g, X, Y)


# %% Imprimir los datos:

plt.figure()
plt.style.use('seaborn')
plt.plot(X_g, Y_g)
plt.plot(X, Y, '.k',markersize = 10)
for i in range(m):
    plt.annotate(f'({X[i]}, {Y[i]})', (X[i]+0.1, Y[i]+0.1))
plt.show()

