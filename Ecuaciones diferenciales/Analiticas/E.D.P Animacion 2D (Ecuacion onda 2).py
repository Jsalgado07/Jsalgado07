'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2022-MM-DD
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as anim
from matplotlib.gridspec import GridSpec
from numpy import sin, cos, pi, e


# %% Definicion de constantes globales y espacions de memoria:

C = 1             # Velocidad de la onda
h = 2             # Amortiguamiento de la cuerda
L = 1             # Longitud de la cuerda

D = 0.1*L         # Area del golpe a la cuerda
N = 1000          # Numero de terminos de la solucion

fps = 60          # frames per second
tT = 1            # Duracion de la animacion [seg] 


# %% Definición de funciones:

def Onda_1(x, t, n_max):              # Ecuacion si amortiguar 
 
    U = [0]                           # Espacio de memoria para la solucion
   
    for n in range(1, n_max):            # Sumatoria de los primeros n terminos    
        Bn = ((L/(C*(n*pi)**2))*      # Coeficiente n-esimo de la sumatoria     
              (cos(n*pi*(1-D)/2)-
               cos(n*pi*(1+D)/2)))   
        u  = (Bn*sin(n*pi*x/L)*       # Termino n-esimo de la sumatoria sin t
              sin(C*n*pi*t/L))   
        U  += u                       # Sumatoria de terminos
   
    return U
        
def Onda_2(x, t, n_max):
    
    U = [0]                           # Espacio de memoria para la solucion
 
    for n in range(1, n_max):         # Sumatoria de los primeros n terminos    
        a = -h/2
        b = n*pi/L
        c = L/2*(1+2*D)
        d = L/2*(1-2*D)
        Bn  = (-2/(C*n*pi*(a**2 + b**2))*
               (b*e**(a*c)*cos(b*c) + a*e**(a*c)*sin(b*c)-
                b*e**(a*d)*cos(b*d) - a*e**(a*d)*sin(b*d)))
    
        Bn = ((L/(C*(n*pi)**2))*      # Coeficiente n-esimo de la sumatoria     
              (cos(n*pi*(1-D)/2)-
              cos(n*pi*(1+D)/2)))   
        u  = (Bn*e**(-h*x/2)*         # Termino n-esimo de la sumatoria sin t
              sin(n*pi*x/L)*
              sin(C*n*pi*t/L))         
            
        U  += u                       # Sumatoria de terminos
    
    return U


# %% Programa principal:

X_g = np.linspace(0, L, 1000)


# %% Imprimir los datos:

Fig = plt.figure(figsize = (10, 10))
Gs  = GridSpec(2, 1, figure = Fig)

Ax1 = Fig.add_subplot(Gs[0,0])

Ax2 = Fig.add_subplot(Gs[1,0])


def Animacion(ti):

    t = ti/fps    

    Ax1.clear()
    Ax2.clear()
    
    Y_g = Onda_1(X_g, t, N)    
    Ax1.plot(X_g, Y_g) 
    
    Y_g = Onda_2(X_g, t, N)    
    Ax2.plot(X_g, Y_g) 
    
    Ax1.set_xlim(0, L)
    Ax2.set_xlim(0, L)
    Ax1.set_ylim(-0.2, 0.2)
    Ax2.set_ylim(-0.2, 0.2)

    return
        
Anim = anim(Fig, Animacion, frames = fps*tT, interval = 1/fps)
Anim.save('E.D.P Animacion 2D (Ecuacion onda 2).gif', fps = fps)

plt.show()



















