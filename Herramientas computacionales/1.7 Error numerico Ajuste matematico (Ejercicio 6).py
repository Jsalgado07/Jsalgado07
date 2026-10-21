'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-MM-DD
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt

from numpy import arange, pi, sin, cos

# %% Definicion de constantes globales y espacions de memoria:

c = pi/2.0
n = arange(1, 11, 1)
m = arange(10, 0, -1)

x = [10.0**-n,0, 10.0**-n] 


# %% Definición de funciones:

f = lambda x: 1.0 - sin(x)
g = lambda x: cos(x)**2/(1.0 + sin(x))


# %% Programa principal:

x = []
for i in range(2*len(n)+1):
    if i < 10:
        x += [c - 10.0**(-n[i])]    
    elif i == 10:
        x += [c]
    else:
        x += [c + 10.0**(-m[i-11])]

F, G = [], []
for i in x:
     F += [f(i)] 
     G += [g(i)]   

# %% Imprimir los datos:

fig = plt.figure(figsize = (10, 6))
ax  = fig.add_subplot()

ax.set_yscale('log')
ax.set_xscale("symlog")
     
ax.plot(x, F, 'bo')
ax.plot(x, G, 'r--')
ax.set_title(r'Grafica del $f(x) = sin(\pi/2-x)$ ')
ax.set_xlabel('x.')
ax.set_ylabel('f(x)')

plt.grid()
plt.show()






