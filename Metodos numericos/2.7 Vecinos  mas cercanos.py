'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2021-20-12
'''

# %% Importación de librerías:

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# %% Definicion de constantes globales y espacions de memoria:

X = [ 3, 4,  1,  5]
Y = [17, 13, 5, 12]
m = len(X)


# %% Definición de funciones:

def Vecinos_Cercanos(X, Y):
    
    X = np.array(X)
    Y = np.array(Y)   
    P = np.array([X, Y]).T
    P = P[np.lexsort(np.fliplr(P).T)]
    X = P[:, 0]
    Y = P[:, 1]
    
    Dif = (X[1:]+X[:-1])/2
    
    X_g = [P[0, 0]]
    Y_g = [P[0, 1]]
    
    for i in range(m-1):
        X_g += [Dif[i], Dif[i]]
        Y_g += [P[i, 1], P[i+1, 1]]
    X_g += [P[-1, 0]]
    Y_g += [P[-1, 1]]

    return X_g, Y_g


# %% Programa principal:

X_g, Y_g = Vecinos_Cercanos(X, Y)
d = (max(Y_g) - min(Y_g))*0.05


# %% Imprimir los datos:

plt.figure()
plt.rcParams['text.usetex'] = True
plt.style.use('seaborn')
plt.title(r'\bf{Interpolacion con Vecinos mas cercanos}', fontsize = 20)
plt.plot(X_g, Y_g)
plt.plot(X, Y, '.k',markersize = 10)
plt.plot([-100, 100], [0, 0], '--', color = 'gray')
plt.plot([0, 0], [-100, 100], '--', color = 'gray')
for i in range(m):
    plt.annotate(f'$({X[i]}, {Y[i]})$', (X[i]+0.1, Y[i]+0.1))
plt.xlim(min(X)-d, max(X)+d)
plt.ylim(min(Y_g)-d, max(Y_g)+d)
plt.show()


