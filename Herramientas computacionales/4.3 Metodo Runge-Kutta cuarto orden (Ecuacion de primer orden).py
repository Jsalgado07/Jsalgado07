'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-04-12
'''


# %% Importación de librerías:

import matplotlib.pyplot as plt
from numpy import arange, sin


# %% Definicion de constantes globales y espacions de memoria:

h1 = 0.5
h2 = 0.1
h3 = 0.01
h4 = 0.001

a = 0
b = 4
y = 1


# %% Definición de funciones:

def Ec(x, y):
    dy = (1 + 2*x)*(y**sin(x*y))    
    return dy


def RungeKutta4(x0, xf, h, y0):
    
    X = arange(x0, xf, h)
    Y = [y0]
    
    for i in range(len(X)-1):       
        k1 = Ec(X[i], Y[i])
        k2 = Ec(X[i] + h/2, Y[i] + h*k1/2)
        k3 = Ec(X[i] + h/2, Y[i] + h*k2/2)
        k4 = Ec(X[i] + h, Y[i] + h*k3)
        y = Y[i] + 1/6*(k1 + 2*k2 + 2*k3 + k4)*h
        Y  += [y]    
    return X, Y


# %% Programa principal:

X1, Y1 = RungeKutta4(a, b, h1, y)
X2, Y2 = RungeKutta4(a, b, h2, y)
X3, Y3 = RungeKutta4(a, b, h3, y)
X4, Y4 = RungeKutta4(a, b, h4, y)


# %% Imprimir los datos:

Fig = plt.figure(figsize = (10, 6))
Ax  = Fig.add_subplot()

Ax.plot(X1, Y1, '-', label=f'Metodo Runge-Kutta Cuarto orden $h={h1}$')
Ax.plot(X2, Y2, '-', label=f'Metodo Runge-Kutta Cuarto orden $h={h2}$')
Ax.plot(X3, Y3, '-', label=f'Metodo Runge-Kutta Cuarto orden $h={h3}$')
Ax.plot(X4, Y4, '-', label=f'Metodo Runge-Kutta Cuarto orden $h={h4}$')

#Ax.plot(X, f(X), '*-', label = 'Solucion analitica')

plt.legend()
plt.grid()
plt.show()