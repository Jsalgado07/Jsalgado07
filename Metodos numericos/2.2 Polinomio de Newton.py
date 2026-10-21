'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2021-11-08
'''

# %% Importación de librerías:

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


# %% Definicion de constantes globales y espacions de memoria:

X = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Y = [1, 5, 2, 3, 6, 4, 2, 8, 1]
N = len(X)

x = sp.symbols('x')



# %% Definición de funciones:

def Diferencias_finitas(X, Y):
    
    n = len(X)
    if n == 1:
        b = Y[0]
    elif n == 2:
        b = (Y[1]-Y[0])/(X[1]-X[0])
    else:
        b = (Diferencias_finitas(X[1:], Y[1:]) -
            Diferencias_finitas(X[:-1], Y[:-1]))/(X[-1]-X[0])
          
    return b

def Interpolacion_Newton(X, Y):
    
    B = []
    for i  in range(N):
        B += [Diferencias_finitas(X[:i+1], Y[:i+1])]    

    y = 0
    for i in range(N):
        T = B[i]
        for j in range(i):
            T *= (x-X[j])
        y += T
        
    y = sp.expand(y)
    f = sp.lambdify(x, y)
    
    return f, y


# %% Programa principal:

f, y = Interpolacion_Newton(X, Y)


# %% Imprimir los datos:

print('El polinomio interpolado es:\n ', y) # Imprimir el polinomio


# %% Graficar el poligono:

X_g = np.linspace(min(X), max(X), 10000)
Y_g = f(X_g)

plt.style.use('seaborn')
plt.plot(X_g, Y_g)
plt.plot(X, Y, 'k.')
plt.show()



