#IMPORTAR LIBRERIAS 
import numpy as np
import matplotlib.pyplot as plt

'''
lAS FUNCIONES SERAN RECTAS DE LA FORMA:
    ax + by = c
    dx + ey = f
'''

#DEFINIR LA FUNCION
def Solucion_2x2(a, b, c, d, e, f):

    if (a*e - b*d) == 0:
        if (-b*f + c*e) == 0 and (a*f - c*d) == 0:
            print('El sistema tiene infinitas soluciones.')
        else:
            print('El sistema no tiene solucion')

    else:
        x = (-b*f + c*e)/(a*e - b*d)
        y = (a*f - c*d)/(a*e - b*d)
        print('La solucion del sistema es: ', '\nX = ', x, '\nY =',  y)

#LLAMAR LA FUNCION
Solucion_2x2(1, 1, 1, 2, 2, 2)