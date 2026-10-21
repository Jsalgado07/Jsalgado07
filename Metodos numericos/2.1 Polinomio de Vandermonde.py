'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2021-11-03
'''

# %% Importación de librerías:

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# %% Definicion de constantes globales y espacions de memoria:

X = [1, 2, 3, 4, 5]         # Punto conocido en x
Y = [1, 4, 9, 1, 7]        # Punto conocido en y
n = len(X)                  # Tamaño del sistema
y = 0

# %% Definición de funciones:

def Polinomio_interpolado(X, Y):
    
    X = np.array(X)             # Usar arreglos de numpy
    Y = np.array(Y)             # Usar arreglos de numpy
    
    S = (np.ones((n, n))*X).T   # Sistema de ecuaciones
    for i in range(n):
        S[:, i] = S[:, i]**i
        
    c = np.linalg.solve(S, Y)   # Coeficientes del polinomio
    
    y = 0
    for i in range(n):
        y += c[i]*x**i          # Construccion del polinomio
    
    f  = sp.lambdify(x, y)      # Definir y como una funcion

    return f, y

# %% Programa principal:

x = sp.symbols('x')
f, y = Polinomio_interpolado(X, Y)

# %% Imprimir los datos:

print('El polinomio interpolado es:\n ', y) # Imprimir el polinomio

xx = np.linspace(X[0], X[n-1], 1000)        # Grafica
yy = f(xx)

plt.style.use('seaborn')    
plt.plot(xx, yy)                            # Grafica del polinomio
plt.plot(X, Y, 'k.')                        # Grafica de los puntos
plt.show()