'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2022-02-22
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.integrate import dblquad
from numpy import sin, cos, pi, exp
from matplotlib.colors import ListedColormap


# %% Definicion de constantes globales y espacions de memoria:

c = 1             # velocidad de la onda.
h = 0.1           # Friccion del medio.
L = 2             # Longitud de la membrana.

P = 0.1           # Presion del golpe.
p = 1             # Densidad de la membrana.
r = L/20          # Radio de la zona del golpe.

NM_Max = 10       # Numero de terminos en la solucion.

t = 0.25*2        # Tiempo de evaluacion.


# %% Definición de funciones:

def Anm_1(n, m):
    
    Ln  = n*pi/L
    Um  = m*pi/L
    Wnm = (c**2*(Ln+Um)+h**2)**0.5
    
    Cnm = 4*P/(Wnm*pi*(L*r)**2*p + 1e-13)
    
    f = lambda x, y: sin(Ln*x)*sin(Um*y)
        
    Li_x =  L/3 - r
    Ls_x = L/3 + r
    Li_y = lambda x: -(r**2 + (x-L/3)**2)**0.5 + L/3
    Ls_y = lambda x: (r**2 + (x-L/3)**2)**0.5 + L/3
    
    R_1, E_1 = dblquad(f, Li_x, Ls_x, Li_y, Ls_y)
   
    Li_x =  2*L/3 - r
    Ls_x = 2*L/3 + r
    Li_y = lambda x: -(r**2 + (x-2*L/3)**2)**0.5 + 2*L/3
    Ls_y = lambda x: (r**2 + (x-2*L/3)**2)**0.5 + 2*L/3    
    
    R_2, E_2 = dblquad(f, Li_x, Ls_x, Li_y, Ls_y)
    
    Anm = Cnm*(R_1 + R_2) 
    
    return Anm


def Bnm_1(n, m):
    Bnm = 0
    return Bnm


def U(x, y, t, nm_max):
    U = 0
    for n in range(nm_max):
        for m in range(nm_max):
            Ln  = n*pi/L
            Um  = m*pi/L
            Wnm = (c**2*(Ln+Um)+h**2)**0.5    
            u   = (sin(Ln*x)*sin(Um*y)*exp(-h*t)*
                   (Anm_1(n, m)*sin(Wnm*t)+Bnm_1(n, m)*cos(Wnm*t)))
            
            U += u
    
    return U
    

# %% Programa principal:

X_g = np.linspace(0, L, 100)
Y_g = np.linspace(0, L, 100)

X_g, Y_g = np.meshgrid(X_g, Y_g)

U_g = U(X_g, Y_g, t, NM_Max)

Up = cm.get_cmap('PuBu', 128)
Dw = cm.get_cmap('PuBu_r', 128)
NewC = np.vstack((Up(np.linspace(0, 1, 128)), Dw(np.linspace(0, 1, 128))))

Bluess = ListedColormap(NewC, name='Bluess')


# %% Imprimir los datos:

Fig = plt.figure(figsize=(5, 5), dpi = 300)

Ax  = Fig.gca(projection='3d')
Ax.plot_surface(X_g, Y_g, U_g, cmap = Bluess, vmin = -0.8, vmax = 0.8)

Ax.set_xlim(0, L)
Ax.set_ylim(0, L)
Ax.set_zlim(-1,  1)

Ax.set_yticks([])
Ax.set_xticks([])
Ax.set_zticks([])

plt.show()
