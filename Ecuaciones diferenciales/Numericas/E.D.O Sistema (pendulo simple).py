'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2021-12-05
'''

# %% Importación de librerías:
 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani 
import matplotlib.gridspec as grid
from numpy import sin, cos, pi
 

# %% Definicion de constantes globales y espacios de memoria:

G  = 9.8                  # Gravedad
L  = 1                    # Longitud de cuerda
Fr = 0.2                  # Friccion

Ti  = 0                   # Tiempo inicial
Tf  = 20                  # Tiempo final
Ai  = pi - 0.1            # Angulo inicial
Dai = pi                  # Velocidad angular inicial
fps = 30


# %% Definición de funciones:

def Ecuacion_diferencial(a, da):
    d2a = - G/L*sin(a) - Fr*da
    return d2a

def Valores_iniciales(a, b, n):
    l = []
    c = int((b-a)/n)
    for i in range(0, c+1):
        d = a + i*n
        l.append(d)
    return l

def Metodo_Euler(n, ti, tf, ai, dai):
    
    dt = (tf-ti)/n
    
    T  = [ti]              # Tiempos
    A  = [ai]              # Angulos
    Da = [dai]             # Velodidades angulares
    
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

N = int(Tf*fps*1e+3)   
Dt = 1/fps
Da, A, T = Metodo_Euler(N, Ti, Tf, Ai, Dai)
        
Da_g = [Da[0]]                      # velocidades angulares para graficar.
A_g  = [A[0]]                       # Angulos para graficar.
T_g  = [T[0]]                       # Tiempos para graficar.
    
for i in range(1, Tf*fps):          # Acortad datos de las listas.
    n = i*1000 
    Da_g += [Da[n]]  
    A_g  += [A[n]]
    T_g  += [T[n]]
    
X_g, Y_g = [], []                   # Coordenadas cartesianas para graficar.
for i in range(len(T_g)):
   X_g += [L*sin(A_g[i])] 
   Y_g += [-L*cos(A_g[i])]

A0  = Valores_iniciales(0, 10, 1)   # Valores iniciales para la solucion

n  = 2000 
dt = (Tf-Ti)/n
U3, V3 = [], []                        # Campo vectorial del diagrama de fase
Y3, X3 = np.mgrid[min(Da)*1.1:max(Da)*1.1:2000j,
                  min(A)*1.1:max(A)*1.1:2000j]
for i in range (n):
    u = []
    v = []
    for j in range(n):
        ai  = X3[i, j]
        dai = Y3[i, j]
        d2a = Ecuacion_diferencial(ai, dai)
        u += [dai*dt]
        v += [d2a*dt]
    U3 += [u]
    V3 += [v]
U3 = np.array(U3)
V3 = np.array(V3)

# %% Imprimir los datos:
    
Color_Fondo = '#191919'
Color_Masa  = '#307B8C'
Color_Curva = '#A9CBD9'
Color_Campo = '#193C40'
Color_Letra = '#D0E9F2'

plt.rcParams['text.usetex'] = True
Fig = plt.figure(constrained_layout = True, figsize = (12, 8),
                 tight_layout=True, facecolor = Color_Fondo)
Gs  = grid.GridSpec(2, 2, figure= Fig)

Fig.suptitle(r"\bf{Pendulo simple}" + "\n" +
             r"\bf{Analisis numerico del sistema}" + "\n" + f"${N}$" +
             r"\bf{ particiones}", fontsize = 20, color = Color_Letra)

plt.style.use('dark_background')

Ax1 = Fig.add_subplot(Gs[:, 0], facecolor = Color_Fondo)
Ax1.set_xticks([])
Ax1.set_yticks([])
Ax1.set_xlim(-L*1.1, L*1.1)
Ax1.set_ylim(-1.45, 1.05)
Ax1.text(0.05, 0.05,
         r"$\frac{d^2\theta}{dt^2} = -0.2\frac{d\theta}{dt}-9.8\sin(\theta)$",
         fontsize = 15, math_fontfamily='cm', transform = Ax1.transAxes,
         color = Color_Letra)
Ax1.plot([-0.2, 0.2], [0, 0], color = Color_Masa, linewidth = 5)
Masa_Ax1,    = Ax1.plot([], [], 'o', color = Color_Masa, markersize = 10)
Cuerda_Ax1,  = Ax1.plot([], [], color = Color_Curva)
Tiempo_Ax1   = Ax1.text(0.05, 0.12, '', transform = Ax1.transAxes, 
                        fontsize =14, color = Color_Letra)

Ax2 = Fig.add_subplot(Gs[0, 1:], facecolor = Color_Fondo)
Ax2.set_title(r'\bf{Diagrama} $\theta$ \bf{vs} $t$', color = Color_Letra, 
              fontsize = 15)
Ax2.set_xlabel(r'\bf{Tiempo [s]}', color = Color_Letra)
Ax2.set_ylabel(r'\bf{Posicion angular [rad]}', color = Color_Letra)
Ax2.set_xlim(-1, Tf)
Ax2.set_ylim(-1, max(A)*1.1)
Ax2.plot([0, 0], [-100, 100], '--', color = 'gray')     # Eje y
Ax2.plot([-100, 100], [0, 0], '--', color = 'gray')     # Eje y
for i in range(len(A0)):                                # curva de soluciones sombra
    da, a, t = Metodo_Euler(1000, Ti, Tf, A0[i], Dai)
    Ax2.plot(t, a, color = Color_Campo, linewidth = 0.7)
Ax2.plot(T_g, A_g, color = Color_Curva)                     # Curva de solucion.
Masa_Ax2,  = Ax2.plot([], [], 'o', color = Color_Masa, markersize = 10)

Ax3 = Fig.add_subplot(Gs[1, 1], facecolor = Color_Fondo)
Ax3.set_title(r'\bf{Diagrama} $\frac{d\theta}{dt}$ \bf{vs} $\theta$', 
              Color = Color_Letra, fontsize = 15)
Ax3.set_xlabel(r'\bf{Posicion angular [rad]}', Color = Color_Letra)
Ax3.set_ylabel(r'\bf{Velocidad angular [rad/s]}', Color = Color_Letra)
Ax3.set_xlim(min(A)*1.1,  max(A)*1.1)
Ax3.set_ylim(min(Da)*1.1, max(Da)*1.1)
Ax3.plot(A_g, Da_g, color = Color_Curva)
Ax3.streamplot(X3, Y3, U3, V3, linewidth = 0.7, density = 1, color = Color_Campo)
Ax3.plot([0, 0], [-100, 100], '--', color = 'gray')     # Eje y
Ax3.plot([-100, 100], [0, 0], '--', color = 'gray')     # Eje y

Masa_Ax3,  = Ax3.plot([], [], 'o', color = Color_Masa, markersize = 10)

def Animacion(i):
    
    Tiempo_Ax1.set_text(f'$Tiempo:$ ${round(i*Dt, 1)}$ $segundos$')
    Masa_Ax1.set_data(X_g[i], Y_g[i])
    Cuerda_Ax1.set_data([0, X_g[i]], [0, Y_g[i]])
    Masa_Ax2.set_data(T_g[i], A_g[i])
    Masa_Ax3.set_data(A_g[i], Da_g[i])
  
    return (Masa_Ax1, Masa_Ax2, Masa_Ax3, Cuerda_Ax1)

Anim  = ani.FuncAnimation(Fig, Animacion, frames = fps*Tf, interval = Dt) 
#Anim.save('pendulo simple.gif', fps = fps)
plt.show()
