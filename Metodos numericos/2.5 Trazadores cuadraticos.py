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

X = [3.0, 4.5, 7.0, 9.0, 4, 10]
Y = [2.5, 1.0, 2.5, 0.5, 5, 2 ]
m = len(X)
n = (m-1)


# %% Definición de funciones:

def Trazadores_cuadraticos(X_g, X, Y):
        
    x = sp.symbols('x')
    
    X = np.array(X, dtype = float)
    Y = np.array(Y, dtype = float)
    P = np.array([X, Y]).T
    P = P[np.lexsort(np.fliplr(P).T)]
    X = P[:, 0]
    Y = P[:, 1]
    
    M = np.zeros((3*n, 3*n))
    C = np.array([0]*3*n, dtype = float)
    
    M[0, 0] = 1
    
    for i in range(n-1):                    # Condicion de las derivadas
        for j in range(2):
            M[1+i, j+i] = (-1)**j*2*X[1+i]
            M[1+i, j+n+i] = (-1)**j
           
    for i in range(n+1):                    # condicion de los puntos
        for j in range(3):
            if i == 0:
                M[n, n*j] = X[0]**(abs(j-2))  
                C[n] = Y[0]
            elif i == (n):
                k = 2*i-1
                M[n+k, n*j+i-1] = X[i]**(abs(j-2)) 
                C[n+k] = Y[i]
            else:
                k = 2*i-1
                M[n+k, n*j+i-1] = X[i]**(abs(j-2)) 
                M[n+k+1, n*j+i] = X[i]**(abs(j-2))
                C[n+k]   = Y[i]
                C[n+k+1] = Y[i]
           
    A = np.linalg.solve(M, C)                   # Resolver el sistema
    X_g = np.linspace(min(X), max(X), 1000)     # Evaluar para cada dominio
    Y_g = [Y[0]]
    for i in range(n):
        f = A[i]*x**2 + A[i+n]*x + A[i+2*n]
        f = sp.lambdify(x, f)
        for j in X_g:
            if j <= X[i+1] and j > X[i]:
                Y_g += [f(j)]
    
    return Y_g


# %% Programa principal:

X_g = np.linspace(min(X), max(X), 1000)
Y_g = Trazadores_cuadraticos(X_g, X, Y)


# %% Imprimir los datos:

d = (max(Y_g) - min(Y_g))*0.05
plt.rcParams['text.usetex'] = True
plt.figure()
plt.style.use('seaborn')
plt.title(r'\bf{Interpolacion con trazarores cuadraticos}', fontsize = 20)
plt.plot(X_g, Y_g)
plt.plot(X, Y, '.k',markersize = 10)
plt.plot([-100, 100], [0, 0], '--', color = 'gray')
plt.plot([0, 0], [-100, 100], '--', color = 'gray')
for i in range(m):
    plt.annotate(f'$({X[i]}, {Y[i]})$', (X[i]+0.1, Y[i]+0.1))
plt.xlim(min(X)-d, max(X)+d)
plt.ylim(min(Y_g)-d, max(Y_g)+d)
plt.show()

