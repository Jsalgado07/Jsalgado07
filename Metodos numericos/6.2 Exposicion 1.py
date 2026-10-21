'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2022-01-31
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani 
import matplotlib.gridspec as grid
from numpy import sin, cos, pi


# %% Definicion de constantes globales y espacions de memoria:

G  = 9.8                  # Gravedad
L  = 1                    # Longitud de cuerda
Fr = 0.2                  # Friccion

Ti  = 0                   # Tiempo inicial
Tf  = 20                  # Tiempo final
Ai  = pi - 0.1            # Angulo inicial
Dai = pi                  # Velocidad angular inicial


fps = 30                  # Tasas de refresco


# %% Definición de funciones:

def Ecuacion_diferencial(a, da):
    d2a = - G/L*sin(a) - Fr*da
    return d2a

def Metodo_Euler(n, ti, tf, ai, dai):
    
    dt = (tf-ti)/n
    
    T  = [ti]              # Tiempos.
    A  = [ai]              # Angulos.
    Da = [dai]             # Velodidades angulares.
    
    for i in range (n):
        d2a = Ecuacion_diferencial(ai, dai)
        da  = dai + d2a*dt
        a   = ai  + da*dt
        t   = ti  + dt
        
        Da += [da]
        A  += [a]
        T  += [t]
        
        dai, ai, ti = da, a, t
        
    return Da, A, T


# %% Programa principal:

N = int(Tf*fps*1000)   
Dt = 1/fps
Da, A, T = Metodo_Euler(N, Ti, Tf, Ai, Dai)

Da_g = [Da[0]]                      # velocidades angulares para graficar.
A_g  = [A[0]]                       # Angulos para graficar.
T_g  = [T[0]]                       # Tiempos para graficar.

for i in range(1, Tf*fps):          # Acortar datos de las listas.
    n = i*1000                      # Tomar solo los datos cada mil
    Da_g += [Da[n]]                 
    A_g  += [A[n]]
    T_g  += [T[n]]
    
X_g, Y_g = [], []                   # Coordenadas cartesianas para graficar.

for i in range(len(T_g)):           # Descomponer el angulo
   X_g += [L*sin(A_g[i])]           # Componente en x del angulo
   Y_g += [-L*cos(A_g[i])]          # Componente en y del angulo


# %% Imprimir los datos:

Fig = plt.figure(constrained_layout = True, figsize = (12, 8),
                 tight_layout=True)

Gs  = grid.GridSpec(2, 2, figure= Fig)

Fig.suptitle(f'PENDULO SIMPLE\nAnalisis numerico del sistema\n{N} particiones'
             , fontsize = 20)

plt.style.use('seaborn')

Ax1 = Fig.add_subplot(Gs[:, 0])
Ax1.set_xticks([])
Ax1.set_yticks([])
Ax1.set_xlim(-L*1.1, L*1.1)
Ax1.set_ylim(-1.45, 1.05)
Ax1.plot([-0.2, 0.2], [0, 0], linewidth = 5)
Masa_Ax1,    = Ax1.plot([], [], 'o', markersize = 10)
Cuerda_Ax1,  = Ax1.plot([], [],)
Tiempo_Ax1   = Ax1.text(0.05, 0.12, '', transform = Ax1.transAxes, 
                        fontsize = 14)

Ax2 = Fig.add_subplot(Gs[0, 1:])
Ax2.set_title('Diagrama de fase', fontsize = 15)
Ax2.set_xlabel('Tiempo [s]')
Ax2.set_ylabel('Posicion angular [rad]')
Ax2.set_xlim(-1, Tf)
Ax2.set_ylim(-1, max(A)*1.1)
Ax2.plot([0, 0], [-100, 100], '--', color = 'gray')     # Eje y
Ax2.plot([-100, 100], [0, 0], '--', color = 'gray')     # Eje X
Ax2.plot(T_g, A_g)                                      # Curva de solucion.
Masa_Ax2,  = Ax2.plot([], [], 'o', markersize = 10)

Ax3 = Fig.add_subplot(Gs[1, 1])
Ax3.set_title('Diagrama de fase', fontsize = 15)
Ax3.set_xlabel('Posicion angular')
Ax3.set_ylabel('Velocidad angular')
Ax3.set_xlim(min(A)*1.1,  max(A)*1.1)
Ax3.set_ylim(min(Da)*1.1, max(Da)*1.1)
Ax3.plot([0, 0], [-100, 100], '--', color = 'gray')     # Eje y
Ax3.plot([-100, 100], [0, 0], '--', color = 'gray')     # Eje X
Ax3.plot(A_g, Da_g)
Masa_Ax3,  = Ax3.plot([], [], 'o', markersize = 10)

def Animacion(i):
    
    Tiempo_Ax1.set_text(f'Tiempo: {round(i*Dt, 1)} segundos')
    Masa_Ax1.set_data(X_g[i], Y_g[i])
    Cuerda_Ax1.set_data([0, X_g[i]], [0, Y_g[i]])
    Masa_Ax2.set_data(T_g[i], A_g[i])
    Masa_Ax3.set_data(A_g[i], Da_g[i])
  
    return

Anim  = ani.FuncAnimation(Fig, Animacion, frames = fps*Tf, interval = Dt) 
#Anim.save('pendulo simple.gif', fps = fps)
plt.show()


