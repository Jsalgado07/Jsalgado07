### IMPORTAR LAS LIBRERIAS ###
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
from numpy import sin, cos, exp, pi

### DEFINIR LAS FUNCIONES DE LA SOLUCION Y SUS DERIVADAS ###
def Fun1(x):
    return sin(x)

def Fun2(x):
    return cos(x)

def Fun3(x):
    return 0
    
def Df(f, x):
    return derivative(f, x, dx=1e-10)

### DEFINIR LA LISTA DE VALORES INICIALES ###
def Valores_iniciales(a, b, n):
    l = []
    c = int((b-a)/n)
    for i in range(0, c+1):
        d = a + i*n
        l.append(d)
    return l

### DEFINIR LOS VALORES DEL P.V.I ###
a, b, n = -10, 10, 2
x0, y1 = 0.0001, 1
y0 = Valores_iniciales(a, b, n)

### CICLO DE IMPRESION ###
for i in y0:
    c1 = (i*Df(Fun2,x0) - y1*Fun2(x0) + Df(Fun3,x0)*Fun2(x0) - Fun3(x0)*Df(Fun2,x0))/(Fun1(x0)*Df(Fun2,x0)-Df(Fun1,x0)*Fun2(x0))
    c2 = (y1 - Df(Fun1,x0)*c1 - Df(Fun3,x0))/(Df(Fun2,x0))
    xx = np.linspace(0, 20, 1000)
    y = Fun1(xx)*c1 + Fun2(xx)*c2 + Fun3(xx) 
    plt.style.use('seaborn')
    plt.plot(xx, y, label='y(0) = {}'.format(i))
    plt.ylim(-10, 10)
    plt.xlim(0,20)
#plt.legend()
plt.show()