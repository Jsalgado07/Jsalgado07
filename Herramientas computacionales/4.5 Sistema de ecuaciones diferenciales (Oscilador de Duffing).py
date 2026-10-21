'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-04-17
'''
'''
Sistema de un oscilador forzado.
'''


# %% Importación de librerías:

import matplotlib.pyplot as plt
from numpy import arange, cos


# %% Definicion de constantes globales y espacions de memoria:

h = 0.001

ti = 0
tf = 100

x0 = 0.5      # Posicion
y0 = 0        # velocidad

a = 1
b = 5
c = 3
d = 0.02
w = 1

F = 0.1

# %% Definición de funciones:

def f(t, x, v):     # Derivada en x = Velocidad del oscilador
    return v


def g(t, x, v):     # Derivada en V = aceleracion
    dy = -d*v - a*x - b*x**3 +  c*cos(w*t)     
    return dy


def RungeKutta4(ti, tf, h, v0, x0):
    
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

Ax.plot(T, X, '-k', label='Posicion')
Ax.plot(T, Y, '--r', label='Velocidad')
Ax.set_title('Sistema Oscilador forzado - Soluciones ')
Ax.set_xlabel('Tiempo')
Ax.set_ylabel('Posicion - Velocidad')

plt.legend()
plt.grid()
plt.show()


Fig = plt.figure(figsize = (10, 6))
Ax  = Fig.add_subplot()

Ax.plot(X, Y, 'k', label='Posicion')
Ax.set_title('Sistema Oscilador forzado - Diagrama de Fase ')
Ax.set_xlabel('Posicion')
Ax.set_ylabel('Velocidad')

plt.legend()
plt.grid()
plt.show()

