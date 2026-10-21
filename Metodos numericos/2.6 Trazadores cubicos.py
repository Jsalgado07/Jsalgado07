'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2021-20-12
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

def Trazadores_Cubicos(X_g, X, Y):
        
    x = sp.symbols('x')
    
    X = np.array(X, dtype = float)
    Y = np.array(Y, dtype = float)
    P = np.array([X, Y]).T
    P = P[np.lexsort(np.fliplr(P).T)]
    X = P[:, 0]
    Y = P[:, 1]
    
    M = np.zeros((4*n, 4*n))
    C = np.array([0]*4*n, dtype = float)
    
    M[0, 0] = 6*X[0]
    M[0, n] = 2 
    M[1, n-1] = 6*X[-1]
    M[1, 2*n-1] = 2  
    
    for i in range(2, n+1):
        for j in range(2):
            M[i, j+(i-2)]   = (-1)**j*6*X[i-1]
            M[i, j+n+(i-2)] = (-1)**j*2 
           
    for i in range(n+1, 2*n):
        for j in range(2):
            M[i, j+(i-n-1)]   = (-1)**j*3*X[i-n]**2
            M[i, j+n+(i-n-1)] = (-1)**j*2*X[i-n] 
            M[i, j+2*n+(i-n-1)] = (-1)**j*1 
        
    for i in range(2*n, 4*n):
        for j in range(4):
            if i == (2*n):
                M[i, n*j] = X[0]**(abs(j-3))  
                C[i] = Y[0]
            elif i == (4*n-1):
                M[i, n*j+n-1] = X[-1]**(abs(j-3)) 
                C[i] = Y[-1]
            elif (i%2) == 1:
                M[i, j*n+int((i-1)/2-n)] = X[int((i+1)/2-n)]**(abs(j-3)) 
                M[i+1, j*n+int((i-1)/2-n)+1] = X[int((i+1)/2-n)]**(abs(j-3))
                C[i]   = Y[int((i+1)/2-n)]
                C[i+1] = Y[int((i+1)/2-n)]
    
    A = np.linalg.solve(M, C)
    X_g = np.linspace(min(X), max(X), 1000)
    Y_g = [Y[0]]
    for i in range(n):
        f = A[i]*x**3 + A[i+n]*x**2 + A[i+2*n]*x + A[i+3*n]
        f = sp.lambdify(x, f)
        for j in X_g:
            if j <= X[i+1] and j > X[i]:
                Y_g += [f(j)]

    return Y_g


# %% Programa principal:

X_g = np.linspace(min(X), max(X), 1000)
Y_g = Trazadores_Cubicos(X_g, X, Y)


# %% Imprimir los datos:

d = (max(Y_g) - min(Y_g))*0.05
plt.rcParams['text.usetex'] = True
plt.figure()
plt.style.use('seaborn')
plt.title(r'\bf{Interpolacion con trazarores Cubicos}', fontsize = 20)
plt.plot(X_g, Y_g)
plt.plot(X, Y, '.k',markersize = 10)
plt.plot([-100, 100], [0, 0], '--', color = 'gray')
plt.plot([0, 0], [-100, 100], '--', color = 'gray')
for i in range(m):
    plt.annotate(f'$({X[i]}, {Y[i]})$', (X[i]+0.1, Y[i]+0.1))
plt.xlim(min(X)-d, max(X)+d)
plt.ylim(min(Y_g)-d, max(Y_g)+d)
plt.show()


