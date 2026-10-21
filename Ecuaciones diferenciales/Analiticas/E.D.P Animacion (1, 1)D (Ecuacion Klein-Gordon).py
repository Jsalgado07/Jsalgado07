'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2022-07-17
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import dblquad
from numpy import sin, cos, pi, linspace
from matplotlib.animation import FuncAnimation as Anim


# %% Definicion de constantes globales y espacions de memoria:

m = 1                # Masa del campo 
L = 50

Tt = 5               # Tiempo de evaluacion.
fps = 30             # Fotogramas por segundo
Frames = fps*Tt      # Numero todal de fps


# %% Definición de funciones:

def Campo(x, t):
    
    k = lambda Lambda, X: (sin((Lambda**2 - m**2)**0.5*t)*
                           cos(Lambda*(x - X))*(Lambda**2 - m**2)**-0.5)*0.1
    I, err_1 = dblquad(k, -L, L, -0.5, 0.5)
    
    Campo = 1/(2*pi)*I

    return Campo
    

# %% Programa principal:

X_g = linspace(-L, L, 100)


# %% Imprimir los datos:

Fig = plt.figure(figsize=(10, 6))        # Crear la figura para la animacion
Ax = Fig.add_subplot()                  # Crear la grafica en 3D

def Animacion(T):                       # Funcion que evalua para cada tiempo                       

    Ax.clear()                          # Limpiar la grafia anteior

    t = T/fps                           # Ajustar el tiempo segun los fps
    
    Campo_g = []
    
    for i in X_g:
    
        campo_g = Campo(i, t)             # Valor de U para cada tiempo
        Campo_g += [campo_g]
    

    t = round(t, 1)                     # Redondear el tiempo para el titulo 
   
    Ax.set_title(f'Tiempo: {t}')        # Titulo de la grafica
    Ax.plot(X_g, Campo_g)                   # Acortar los colores hasta z =  0.8
              
    Ax.set_xlim(-L, L)       # Limite en x desde x = 0 hasta x = L
    Ax.set_ylim(-10, 10)         # Limite en y desde y = 0 hasta y = L
    
    # Ax.set_xticks([])       # Borrar la cuadricula en x
    # Ax.set_yticks([])       # Borrar la cuadricula en y
    
    return 

Animacion  = Anim(Fig, Animacion, frames = Frames, interval = 1000/fps )
Animacion.save('E.D.P Ecuacion de Klein-Gordon (1, 1) D.gif', fps = fps)
plt.show()


