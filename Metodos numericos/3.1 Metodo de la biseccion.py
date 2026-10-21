'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2021-??-??
'''

# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt
from numpy import exp, sin, pi

# %% Definicion de constantes globales y espacions de memoria:

Xd = 2.5                     # Valor de x derecho
Xi = 2                     # Valor de x izquierdo
T = 0.0000000000001        # Tolerancia

F = lambda x: sin(x)

# %% Definición de funciones:

def Raiz_Biseccion(xd, xi, f, t):
        
    n = 0
    xp = (xd + xi)/2
    
    while True:
        n  += 1
        x0 = xp
        if   f(xd)*f(xp) < 0:
            xi = xp
        elif f(xd)*f(xp) > 0:
            xd = xp
        
        xp = (xd + xi)/2
        e  = abs((x0-xp)/xp)
        if e < t:
            break

    return xp, n

# %% Programa principal:
    
Xp, n = Raiz_Biseccion(Xd, Xi, F, T)

M = abs(Xi-Xd)*0.2

print(f'\nSe hicieron {n} iteraciones')
print(f'La raiz de la funcion entre {Xi} y {Xd} es:\n  x = {Xp}')

# %% Imprimir los datos:

xx = np.linspace(Xi-M, Xd+M, 1000)
yy  = F(xx)


plt.style.use('seaborn')
plt.plot(xx, yy)
plt.plot(Xp, 0, 'k.')
plt.plot(Xi, F(Xi), 'r.')
plt.plot(Xd, F(Xd), 'r.')

plt.show()

