'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-04-12
'''


# %% Importación de librerías:

import matplotlib.pyplot as plt

from numpy import arange, sin


# %% Definicion de constantes globales y espacions de memoria:

h = 0.01
a = 0
b = 5
y = 1
f = lambda x: x**4/4 + x**3/2 + x**2*5/4 + x + 1 


# %% Definición de funciones:

def Ec(x, y):
    dy = (1 + 2*x)*(y**sin(x*y))    
    return dy


def Euler(x0, xf, h, y0):
    
    dy = Ec(x0, y0)    
    X = arange(x0, xf, h)
    Y = [y0]
    
    for i in range(len(X)-1):        
        y = Y[i] + dy*h
        Y  += [y]
        dy = Ec(X[i+1], y)
    
    return X, Y


def RungeKutta2(x0, xf, h, y0):
    
    X = arange(x0, xf, h)
    Y = [y0]
    
    for i in range(len(X)-1):       
        k1 = Ec(X[i], Y[i])
        k2 = Ec(X[i] + h/2, Y[i] + h*k1/2)
        y = Y[i] + k2*h
        Y  += [y]    
    return X, Y


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

X1, Y1 = Euler(a, b, h, y)
X2, Y2 = RungeKutta2(a, b, h, y)
X4, Y4 = RungeKutta4(a, b, h, y)





# %% Imprimir los datos:

Fig = plt.figure(figsize = (10, 6))
Ax  = Fig.add_subplot()

Ax.plot(X4, Y4, 'o-', label=f'Metodo Runge-Kutta Cuarto orden $h={h}$')
Ax.plot(X2, Y2, 'o-', label=f'Metodo Runge-Kutta Segundo orden $h={h}$')
Ax.plot(X1, Y1, 'o-', label=f'Metodo Runge-Kutta Primer orden $h={h}$')
# Ax.plot(X1, f(X1), '*-', label = 'Solucion analitica')

Ax.set_title('Comparativa a soluciones aproximadas y analitica')

plt.legend()
plt.grid()
plt.show()


# Fig = plt.figure(figsize = (10, 6))
# Ax  = Fig.add_subplot()

# Ax.plot(X4, f(X1)-Y4, 'o-', label=f'Metodo Runge-Kutta Cuarto orden $h={h}$')
# Ax.plot(X2, f(X1)-Y2, 'o-', label=f'Metodo Runge-Kutta Segundo orden $h={h}$')
# Ax.plot(X1, f(X1)-Y1, 'o-', label=f'Metodo Runge-Kutta Primer orden $h={h}$')

# Ax.set_title('Error relativo en las diferentes soluciones')

# plt.legend()
# plt.grid()
# plt.show()
