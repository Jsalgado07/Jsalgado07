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
from numpy import sin, cos, pi, exp, vstack
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation as Anim


# %% Definicion de constantes globales y espacions de memoria:

c = 1                # velocidad de la onda.
h = 0.1              # Friccion del medio.
L = 2                # Longitud de la membrana.

P = 0.15             # Presion del golpe.
p = 1                # Densidad de la membrana.
r = L/20             # Radio de la zona del golpe.

NM_Max = 10          # Numero de terminos en la solucion.

Tt = 5               # Tiempo de evaluacion.
fps = 30             # Fotogramas por segundo
Frames = fps*Tt      # Numero todal de fps


# %% Definición de funciones:

def Anm_1(n, m):                        # Calculo de la constante Anm
    
    Ln  = n*pi/L                        # Constante Lamnda sub n
    Um  = m*pi/L                        # Constante Mu sub m
    Wnm = (c**2*(Ln+Um)+h**2)**0.5      # Constante de frecuencias W sub nm
    
    Cnm = 4*P/(Wnm*pi*(L*r)**2*p        # Constante global de las integrales
               + 1e-13) 
    
    f = lambda x, y: sin(Ln*x)*sin(Um*y)    # Funcion general a integrar 
        
    Li_x = L/3 - r                          # Limite inferior constante
    Ls_x = L/3 + r                          # Limite superior constante
    Li_y = lambda x: -(r**2 + (x-L/3)       # Limite inferior varianble
                       **2)**0.5 + L/3  
    Ls_y = lambda x: (r**2 + (x-L/3)        # Limite superior variable
                      **2)**0.5 + L/3
    
    R_1, E_1 = dblquad(f, Li_x, Ls_x,       # Calculo numerico para la primera
                       Li_y, Ls_y)          # integral doble
   
    Li_x =  2*L/3 - r                       # Limite superior constante
    Ls_x = 2*L/3 + r                        # Limite inferior constante
    Li_y = lambda x: -(r**2 + (x-2*L/3)     # Limite superior variable
                       **2)**0.5 + 2*L/3
    Ls_y = lambda x: (r**2 + (x-2*L/3)      # Limite inferior variable
                      **2)**0.5 + 2*L/3    
    
    R_2, E_2 = dblquad(f, Li_x, Ls_x,       # Calculo numerioco para la segunda
                       Li_y, Ls_y)          # ingral doble
        
    Anm = Cnm*(R_1 + R_2)                   # Valor final para constante Anm
    
    return Anm


def Bnm_1(n, m):         # Calculo de la constante Bnm           
    Bnm = 0              # La constante vale cero para cualquier n y m
    return Bnm


def U(x, y, t, nm_max):                    # Funcion final de la solucion
    U = 0
    for n in range(nm_max):                # Sumatoria en n       
        for m in range(nm_max):            # Sumatoria en m
            Ln  = n*pi/L                   # Valor para la constante Lamnda n      
            Um  = m*pi/L                   # Valor para la constente Mu m   
            Wnm = (c**2*(Ln+Um)+           # Valor para la frecuencia W nm   
                   h**2)**0.5             
            u = (sin(Ln*x)*sin(Um*y)*      # Termino nm_esimo para la funcion
                 exp(-h*t)*
                 (Anm_1(n, m)*sin(Wnm*t) +
                 Bnm_1(n, m)*cos(Wnm*t)))
            
            U += u                         #  Suma de todos los terminos para u                
    
    return U


# %% Programa principal:

X_g = np.linspace(0, L, 100)              # Espacio de evaluacion para x
Y_g = np.linspace(0, L, 100)              # Espacio de evaluacion para y

X_g, Y_g = np.meshgrid(X_g, Y_g)          # Plano x, y de evaluacion

Up = cm.get_cmap('PuBu', 128)             # Definir el color nuevo inicial
Dw = cm.get_cmap('PuBu_r', 128)           # Definir el color nuevo final
NC = vstack((Up(np.linspace(0, 1, 128)),  # Unir el color inicial con el final
            Dw(np.linspace(0, 1, 128))))

B = ListedColormap(NC, name='B')          # Nombrar el color nuevo 


# %% Imprimir los datos:

Fig = plt.figure(figsize=(9, 9))        # Crear la figura para la animacion
Ax = Fig.gca(projection='3d')           # Crear la grafica en 3D

def Animacion(T):                       # Funcion que evalua para cada tiempo                       

    Ax.clear()                          # Limpiar la grafia anteior

    t = T/fps                           # Ajustar el tiempo segun los fps
    U_g = U(X_g, Y_g, t, NM_Max)        # Valor de U para cada tiempo
   
    t = round(t, 1)                     # Redondear el tiempo para el titulo 
   
    Ax.set_title(f'Tiempo: {t}')        # Titulo de la grafica
    Ax.plot_surface(X_g, Y_g, U_g,      # Gragica se la membrana   
                    cmap = B,           # Paleta de colores modificada
                    vmin = -0.8,        # Acortar los colores desde z = -0.8   
                    vmax=0.8)           # Acortar los colores hasta z =  0.8
              
    Ax.set_xlim(0, L)       # Limite en x desde x = 0 hasta x = L
    Ax.set_ylim(0, L)       # Limite en y desde y = 0 hasta y = L
    Ax.set_zlim(-1,  1)     # Limite en z desde z = -1 hasta z = 1    
    
    Ax.set_xticks([])       # Borrar la cuadricula en x
    Ax.set_yticks([])       # Borrar la cuadricula en y
    Ax.set_zticks([])       # Borrar la cuadricula en z
    
    return 

Animacion  = Anim(Fig, Animacion, frames = Frames, interval = 1000/fps )
Animacion.save('E.D.P Animacion 3D (Membrana vibrante 3).gif', fps = fps)
plt.show()