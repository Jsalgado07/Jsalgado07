### IMPORTAR LAS LIBRERIAS ###

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.misc import derivative


### DEFINIR LAS FUNCIONES DE LA SOLUCION Y SUS DERIVADAS ###

def Fun1(x):
    return np.exp(-3*x)*np.sin(x)

def Fun2(x):
    return np.exp(-3*x)*np.cos(x)

def Fun3(x):
    return (-25*np.cos(4*x))/102 +(50/51)*np.sin(4*x)

def Df(f, x):
    return derivative(f, x, dx=1e-10)


### DEFINIR LOS VALORRES DEL P.V.I ###

x0 = 0
y0 = 0
y1 = [-10, -5, -3, -1, 0, 1, 3, 5, 10]


### CICLO DE IMPRESION ###

for i in y1:
    c1 = (y0*Df(Fun2,x0) - i*Fun2(x0) + Df(Fun3,x0)*Fun2(x0) - Fun3(x0)*Df(Fun2,x0))/(Fun1(x0)*Df(Fun2,x0)-Df(Fun1,x0)*Fun2(x0))
    c2 = ((i - Df(Fun1,x0)*c1 - Df(Fun3,x0))/Df(Fun2,x0))
    xx = np.linspace(0, 3, 1000)
    y = Fun1(xx)*c1 + Fun2(xx)*c2 + Fun3(xx) 
    plt.plot(xx, y, label='y(0) = {}'.format(i))
    plt.ylim(-2, 2)
    
plt.legend()