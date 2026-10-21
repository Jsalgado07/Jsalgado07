'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2022-08-05
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt

from numpy import sin, cos, pi, e, linspace
from matplotlib.animation import FuncAnimation as Anim

# %% Definicion de constantes globales y espacions de memoria:

a, b = 10, 10
c = 1

N = 100

X1 = [1, 2, 5, 6, 6, 6]
X2 = [4, 3, 6, 8, 8, 8]

Y1 = [7, 1, 1, 7, 4, 1]
Y2 = [8, 7, 8, 8, 5, 2]

Tt = 5               # Tiempo de evaluacion.
fps = 30             # Fotogramas por segundo
Frames = fps*Tt      # Numero todal de fps


# %% Definición de funciones:

    
def Anm(n, m):
    Anm = 0
    for i in range(len(X1)):
        anm  = 4/(n*m*pi**2)*((cos(n*pi*X1[i]/a) - cos(n*pi*X2[i]/a))*
                              (cos(m*pi*Y1[i]/b) - cos(m*pi*Y2[i]/b)))
        Anm += anm
    return Anm

def Campo(x, y, t, N):
    
    U = 0
    
    for n in range(N):
        for m in range(N):
            n = n + 1
            m = m + 1
            w = ((n*pi/a)**2 + (m*pi/b)*2)**0.5  
            u = Anm(n,m)*sin(n*pi*x/a)*sin(m*pi*y/b)*e**(w**2*c**2*t)
            
            U += u   
        
    return U


# %% Programa principal:

X = linspace(0, a, 1000)
Y = linspace(0, b, 1000)

X_g, Y_g = np.meshgrid(X, Y)

U_g = Campo(X_g, Y_g, 0, N)


# %% Imprimir los datos:

Fig = plt.figure(figsize = (10, 10))    
Ax  = Fig.add_subplot()

Ax.contourf(X_g, Y_g, U_g, 50)


plt.show() 









