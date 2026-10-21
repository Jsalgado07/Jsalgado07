'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2022-02-18
'''


# %% Importación de librerías:

import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation as Anim
from numpy import sin, cos, pi, exp


# %% Definicion de constantes globales y espacions de memoria:

c = 1             # velocidad de la onda
h = 0.1           # Friccion del medio
L = 2             # Longitud de la membrana

P = 0.3           # Presion del golpe  
p = 1             # Densidad de la membrana
e = L/10          # Radio de la zona del golpe

NM_Max = 10       # Numero de terminos en la solucion

fps = 60 


# %% Definición de funciones:

def Anm_1(n, m):
    
    Ln  = n*pi/L
    Um  = m*pi/L
    Wnm = (c**2*(Ln+Um)+h**2)**0.5
    Cnm = 4*P/(Wnm*m*L*(pi*e)**2*p + 1e-13)
    # x = sp.symbols('x') 
    
    def f(x):
        f = sin(Ln*x)*(cos(Um*(-(e**2 - (x-L/2)**2)**0.5 + L/2))-
                       cos(Um*((e**2 - (x-L/2)**2)**0.5 + L/2)))
        return f 
    
    I, Er = integrate.quad(f, L/2-e, L/2+e)
    Anm = Cnm*I 
    
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
            u = sin(Ln*x)*sin(Um*y)*exp(-h*t)*(Anm_1(n, m)*sin(Wnm*t)+
                                               Bnm_1(n, m)*cos(Wnm*t))
            
            U += u
        
    return U


# %% Programa principal:

X_g = np.linspace(0, L, 100)
Y_g = np.linspace(0, L, 100)

X_g, Y_g = np.meshgrid(X_g, Y_g)


# %% Imprimir los datos:

Fig = plt.figure(figsize=(9, 9))
Ax = Fig.gca(projection='3d')

Up = cm.get_cmap('PuBu', 128)
Dw = cm.get_cmap('PuBu_r', 128)
NewC = np.vstack((Up(np.linspace(0, 1, 128)), Dw(np.linspace(0, 1, 128))))
Bluess = ListedColormap(NewC, name='Bluess')

def Animacion(T):

    Ax.clear()

    t = 6*T/fps
    U_g = U(X_g, Y_g, t, NM_Max)
   
    Ax.set_title(f'Tiempo: {round(t, 2)}')
    Ax.plot_surface(X_g, Y_g, U_g, cmap = Bluess, vmin = -0.8, vmax=0.8)
   
    Ax.scatter(1, 1, 0.8)    
    Ax.set_xlim(0, L)
    Ax.set_ylim(0, L)
    Ax.set_zlim(-1,  1)
    
    Ax.set_yticks([])
    Ax.set_xticks([])
    Ax.set_zticks([])
    
    return 

Animacion  = Anim(Fig, Animacion, frames = 60, interval = 0 )
Animacion.save('E.D.P Animacion 3D (Membrana vibrante 3).gif', fps = fps)
plt.show()

