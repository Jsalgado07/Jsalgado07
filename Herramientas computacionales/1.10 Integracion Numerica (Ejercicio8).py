'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-MM-DD
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt

from scipy import optimize as op


# %% Definicion de constantes globales y espacions de memoria:

Datos = np.loadtxt('accel.txt')

t = Datos[:, 0]
a = Datos[:, 1]

n = len(t)


# %% Definición de funciones:

def Trapezoid(x, y, n):
     
    area = 0
    for k in range(1, n):
        dx = x[k+1] - x[k]
        area += (dx/2)*(y[k] + y[k+1]) 
        
    return area

def Cuadratic(x, a, b, c, ):
    y = a*x**2 + b*x + c
    return y


# %% Programa principal:

v = []
for i in range(n):
    v += [Trapezoid(t, a, i)]
    
x = []
for i in range(n):
    x += [Trapezoid(t, v, i)]

par_x, cov_x = op.curve_fit(Cuadratic, t, x)


# %% Imprimir los datos:

fig = plt.figure(figsize = (8, 6))
ax1 = fig.add_subplot()
ax1.plot(t, a, '-o', color='purple', label='Datos experimentales de aceleracion')
ax1.set_xlabel('Tiempo [s]')
ax1.set_ylabel('Aceleracion [m/s^2]')
plt.legend()
plt.show()

fig = plt.figure(figsize = (8, 6))
ax2 = fig.add_subplot()
ax2.plot(t, v, '-o', color='purple', label='Datos de integracion numerica')
ax2.set_xlabel('Tiempo [s]')
ax2.set_ylabel('Velocidad [m/s]')
plt.legend()
plt.show()


fig = plt.figure(figsize = (8, 6))
ax3 = fig.add_subplot()
ax3.plot(t, Cuadratic(t, *par_x), label = 'Ajuste cubico' )
ax3.plot(t, x, '-o', color='purple', label='Datos de integracion numerica')
ax3.set_xlabel('Tiempo [s]')
ax3.set_ylabel('Posicion [m]')
plt.legend()
plt.show()

