'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2022-01-25
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as Anim
from numpy import sin, cos, pi
from math import factorial as fac



# %% Definicion de constantes globales y espacions de memoria:

P = 1
C = 1
E = 1
p = 1
A = 1


L = [2.4, 5.1, 8.657, 11.789, 14.931, 18.068, 21.219, 24.348, 27.499,
     30.627, 33.764, 36.906]

N = len(L)
K = int(120)


# %% Definición de funciones:

def Bessel(x, n, k_max):            # Funcion de Bessel

    J = 0

    for k in range(0, k_max):
        c = (((-1)**k))/(fac(k)*fac(n+k))
        j = c*(x/2)**(n+2*k)
        J = j + J 

    return J

def Solution(x, y, t, n_max, k_max):
    
    r = (x**2 + y**2)**(1/2)
    c = 2*P/(C*pi*E*p)
    U = 0
    
    for n in range(n_max):
        u = (Bessel((L[n]*E/A), 1, k_max)/((L[n]*Bessel(L[n], 1, k_max))**2)
             *Bessel(L[n]*r/A, 0, k_max)*sin(L[n]*t*C/A))
        U += c*u
        
    return U


# %% Programa principal:

xx1 = np.linspace(-1, 1, 100)
xx2 = np.linspace(0, 2*pi, 100)
yy1 = np.linspace(-1, 1, 100)

X1, Y1 = np.meshgrid(xx1, yy1)

X2 = cos(xx2)
Y2 = sin(xx2)
Z2 = [0.1]*len(xx2)


# %% Imprimir los datos:

Fig = plt.figure(figsize=(9, 9))
Ax = Fig.gca(projection='3d')

def Animacion(t):

    Ax.clear()
        
    Z1 = Solution(X1, Y1, t/50, N, K)
    
   # Ax.plot(X2, Y2, Z2, color = 'black', linewidth = 5)
    Ax.plot_surface(X1, Y1, Z1)
    
    Ax.set_xlim(-1, 1)
    Ax.set_ylim(-1, 1)
    Ax.set_zlim(-0.6, 0.6)
    
    return 

Animacion  = Anim(Fig, Animacion, frames = 600, interval = 1 )
Animacion.save('E.D.P Animacion 3D (Membrana vibrante).gif', fps = 30)
plt.show()
