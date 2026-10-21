'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-04-17
'''
'''
Sistema de Llofka-Volterra, ecuaciones diferenciales de primer orden
acopladas
'''


# %% Importación de librerías:

import matplotlib.pyplot as plt
from numpy import arange


# %% Definicion de constantes globales y espacions de memoria:

h = 0.001

ti = 0
tf = 100

x0 = 30        # Conejos
y0 = 10         # Zorros

a = 1.1
b = 0.4
c = 0.4 
d = 0.1 


# %% Definición de funciones:

def f(t, x, y):
    dx = a*x - b*x*y   
    return dx

def g(t, x, y):
    dy = d*x*y - c*y     
    return dy


def RungeKutta4(ti, tf, h, y0, x0):
    
    T = arange(ti, tf, h)
    
    X = [x0]
    Y = [y0]
    
    for i in range(len(T)-1):     
    
        k1x = f(T[i], X[i], Y[i])
        k1y = g(T[i], X[i], Y[i])
        
        k2x = f(T[i] + h/2, X[i] + h*k1x/2, Y[i] + h*k1y/2)
        k2y = g(T[i] + h/2, X[i] + h*k1x/2, Y[i] + h*k1y/2)
        
        k3x = f(T[i] + h/2, X[i] + h*k2x/2, Y[i] + h*k2y/2)
        k3y = g(T[i] + h/2, X[i] + h*k2x/2, Y[i] + h*k2y/2)
        
        k4x = f(T[i]+ h, X[i] + h*k3x , Y[i] + h*k3y)
        k4y = g(T[i]+ h, X[i] + h*k3x , Y[i] + h*k3y)
        
        x = X[i] + 1/6*(k1x + 2*k2x + 2*k3x + k4x)*h
        y = Y[i] + 1/6*(k1y + 2*k2y + 2*k3y + k4y)*h
        
        X += [x]
        Y += [y]
        
    return T, X, Y


# %% Programa principal:

T, X, Y = RungeKutta4(ti, tf, h, y0, x0)


# %% Imprimir los datos:

Fig = plt.figure(figsize = (10, 6))
Ax  = Fig.add_subplot()

Ax.plot(T, X, '--k', label='Poblacion de Conejos')
Ax.plot(T, Y, '-r', label='Poblacion de Zorroz')
Ax.set_title('Sistema de Loftka-Volterra')
Ax.set_xlabel('Tiempo')
Ax.set_ylabel('Soluciones')

plt.legend()
plt.grid()
plt.show()