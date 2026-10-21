'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-02-17
'''
'''
Masa resorte
'''


# %% Importación de librerías:


import numpy as np
import matplotlib.pyplot as plt


# %% Definicion de constantes globales y espacions de memoria:

print('Vamos a simular un Sistema Masa Resorte.\n')

m = float(input('Ingrese la masa del objeto: '))
k = float(input('Ingrese la constante del resorte: '))
x0 = float(input('Ingrese la posisición inicial: '))

tmax = 8 * np.pi * np.sqrt(m/k)

xx = []
tt = np.linspace(0, tmax, 1000)


# %% Definición de funciones:

def X(t):
    f = x0 * np.cos(np.sqrt(k / m) * t)
    return f


# %% Programa principal:

for t in tt:
    xx.append(X(t))


# %% Imprimir los datos:

plt.figure()
plt.plot(tt, xx)
plt.xlabel('tiempo')
plt.ylabel('pos')
plt.show()


