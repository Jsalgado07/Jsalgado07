#IMPORTAR LIBRERIAS 
import numpy as np
import matplotlib.pyplot as plt

'''
lAS FUNCIONES SERAN RECTAS DE LA FORMA:
    ax + by = c
    dx + ey = f
'''

#DEFINIR LA FUNCION
def Graficar_Rectas(a, b, c, d, e, f):
    x = np.array([-10, 10])
    y1 = (c-a*x)/b
    y2 = (f-d*x)/e

    plt.figure()
    plt.style.use('seaborn')
    plt.plot(x, y1, label='Ecuacion 1: ' f"{a}$x$ + {b}$y$ = {c}")
    plt.plot(x, y2, label='Ecuacion 2: ' f"{d}$x$ + {e}$y$ = {c}")
    plt.legend()
    plt.show()

#LLAMAR LA FUNCION
Graficar_Rectas(1, 1, 1, 2, 2, 3)