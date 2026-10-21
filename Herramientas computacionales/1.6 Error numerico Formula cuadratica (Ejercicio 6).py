'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-02-27
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt


# %% Definicion de constantes globales y espacions de memoria:

a = 1.0
b = 1.0

n = np.arange(1, 11, 1)
c = 10.0**(-n)


# %% Definición de funciones:

def Cuadratica(a, b ,c):
    
    X1 = (-b + (b*b - 4*a*c)**0.5)/(2*a)
    X2 = (-b - (b*b - 4*a*c)**0.5)/(2*a)
    
    Y1 = (-2*c)/(-b + (b*b - 4*a*c)**0.5)
    Y2 = (-2*c)/(-b - (b*b - 4*a*c)**0.5)
    
    diff1 = abs((X1 - Y2))
    diff2 = abs((X1 - Y2))

    return diff1, diff2


# %% Programa principal:

diff1, diff2 = Cuadratica(a, b, c)


# %% Imprimir los datos:

fig = plt.figure(figsize = (10, 5))
ax  = fig.add_subplot() 

ax.set_yscale("logit")
ax.set_xscale("log")
ax.plot(c, diff1, 'ro', label= 'Soluciones positivas.')
ax.plot(c, diff2, 'bo', label= 'Soluciones negativas.')

ax.set_title('Diferencias relativas entre las soluciones de la cuadratica')
ax.set_xlabel('Valor del termino independiente c.')
ax.set_ylabel('Diferencia relativa')

plt.legend()
plt.show()

