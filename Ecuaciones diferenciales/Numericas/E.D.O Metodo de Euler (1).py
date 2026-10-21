### IMPORTAR LIBRERIAS ###
import numpy as np
import matplotlib.pyplot as plt

### DEFINIR ECUACION DIFERENCIAL ###
def Derivada(x, y):
    f = 3.678*x*(1-x)
    return f

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
    a, b, nn = 0.1, 0.2, 0.1
    y0 = Valores_iniciales(a, b, nn)
    x0, xf = 0, 30

    h = (xf-x0)/n
    for j in range(len(y0)):
        xx, yy = [x0], [y0[j]]
        x, y = x0, y0[j]
        for i in range(1, n+1):
            x = x + h
            y = y + Derivada(x, y)*h
            xx.append(x)
            yy.append(y)
        plt.style.use('seaborn')
        plt.plot(xx, yy, label='y(0) = {}'.format(y0[j])) 
    plt.xlim(x0, xf)
    plt.ylim(0,1) 
    #plt.legend()
    plt.show()

Euler(1000)