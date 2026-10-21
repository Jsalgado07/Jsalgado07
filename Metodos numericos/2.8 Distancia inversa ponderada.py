'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2021-20-12
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi


# %% Definicion de constantes globales y espacions de memoria:

X = [-15, -12, -10, 0, 3, 3.5, 7, 8]
Y = [  1,   2,   3, 4, 5,   6, 7, 8]
R = 0.001
G = 2

# %% Definición de funciones:

def Distancia_inversa(X, Y, R, G):
    
    X = np.array(X)             # Convertir a arreglo numpy
    Y = np.array(Y)             # Convertir a arreglo numpy
    n = len(X)                  # Numero de puntos
    
    X_g = np.arange(min(X), max(X)+R, R)*pi/(pi-0.001)
    w = np.zeros(len(X_g))
    for i in range(n):
        d = abs(X[i]-X_g)
        w += 1/(d)**G
    
    Y_g = np.zeros(len(X_g))
    for i in range(n):
        d = abs(X[i]-X_g)
        Y_g += Y[i]/(d**G*w)

    return X_g, Y_g

# %% Programa principal:

X_g, Y_g = Distancia_inversa(X, Y, R, G)
X_g2, Y_g2 = Distancia_inversa(X, Y, R, G)


# %% Imprimir los datos:

d = (max(Y_g) - min(Y_g))*0.05

plt.figure()
plt.rcParams['text.usetex'] = True

plt.style.use('seaborn')
plt.title(r'\bf{Interpolacion Distancia inversa ponderada}', fontsize = 20)

plt.plot(X_g, Y_g)
plt.plot(X, Y, '.k',markersize = 10)
plt.plot([-100, 100], [0, 0], '--', color = 'gray')
plt.plot([0, 0], [-100, 100], '--', color = 'gray')
for i in range(len(X)):
    plt.annotate(f'$({X[i]}, {Y[i]})$', (X[i]+0.1, Y[i]+0.1))
plt.xlim(min(X)-d, max(X)+d)
plt.ylim(min(Y_g)-d, max(Y_g)+d)

plt.show()

