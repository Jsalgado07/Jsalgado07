### IMPORTAR LIBRERIAS ###
import numpy as np
import matplotlib.pyplot as plt
from numpy import exp, sin, cos, e, pi

### DEFINIR SISTEMA DE ECUACIONES DIFERENCIALES ###
def SegDer(x, y, dy): 
    dy2 = - 0.2/1*(dy) - 5/1*(y)
    return dy2

### DEFINIR LOS VALORES INICIALES ###

def Valores_iniciales(a, b, n):
    l = []
    c = int((b-a)/n)
    for i in range(0, c+1):
        d = a + i*n
        l.append(d)
    return l

### DEFINIR EL METODO DE EULER ###

def Euler(n):
    a, b, nn = 1, 1, 1
    dy0 = 0
    y0 = Valores_iniciales(a, b, nn)
    x0, xf = 0, 20
    h = (xf-x0)/n
    for j in range(len(y0)):
        xx, yy = [x0], [y0[j]]
        x, y , dy = x0, y0[j], dy0
        for i in range(1, n+1):
            dy = dy + SegDer(x, y, dy)*h
            y = y + dy*h
            x = x + h
            xx.append(x)
            yy.append(y)
        plt.style.use('seaborn')
        plt.plot(xx, yy, label='y(0) = {}'.format(y0[j])) 
    plt.xlim(x0, xf)
    plt.ylim(-2, 2) 
    #plt.legend()
    plt.show()

Euler(1000000)