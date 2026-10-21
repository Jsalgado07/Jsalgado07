'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2021-12-01
'''

# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt
from numpy import sin


# %% Definicion de constantes globales y espacions de memoria:

Xi = 0
Xf = 10
T = 1e-16
d = 0.01* np.pi/(np.pi+0.00000001)

f = lambda x: x**3 - 3*x**2 - 1


# %% Definición de funciones:

def Falsa_posicion(Xi, Xf, f, T, d):

    I = []        # intervalos
    R = []        # Raices
    while True:
        if f(Xi)*f(Xi+d) <= 0:
            I += [[Xi, Xi+d]]
        Xi += d
        if Xi >= Xf:
            break

    for i in range(len(I)):
        Xi = I[i][0]
        Xf = I[i][1]
        Xp = (Xi+Xf)/2
        while True:
            X0 = Xp
            if f(Xi)*f(Xf) < 0:
                Xf = Xp
            elif f(Xi)*f(Xf) > 0:
                Xi = Xp
                
            Xp = Xf - f(Xf)*f(Xi-Xf)/(f(Xi)-f(Xf))
            E = abs((X0-Xp)/Xp)
            if E < T:
                break
        R += [Xp]
    
    return R


# %% Programa principal:

R = Falsa_posicion(Xi, Xf, f, T, d)

print(f'Las raices de la funcion entre {Xi} y {Xf} son:\n')
for i in range (len(R)):
    r = round(R[i], 3)
    print(f' x{i} = {r}')


# %% Imprimir los datos:

xx = np.linspace(Xi, Xf, 1000)
yy = f(xx)

plt.style.use('seaborn')
plt.plot(xx, yy)
plt.plot(R, [0]*len(R), 'k.')
plt.show()
