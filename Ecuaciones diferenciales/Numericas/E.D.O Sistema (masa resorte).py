'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2021-12-04
'''

# %% Importación de librerías:

import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib.gridspec as grid


# %% Definicion de constantes globales y espacions de memoria:

M  = 1              # Masa en kg
K  = 5              # constante de elasticidad
Fr = 0.2            # Fuerza de friccion
Fx = 0              # Fuerza externa

Ti  = Tii =  0
Tf  = Tff = 20
Yi  = Yii = 1
Dyi = 0 

fps = 30

Dy = [Dyi]
Y  = [Yi]
T  = [Ti]

# %% Definición de funciones:

def Segunda_derivada(t, y, dy): 
    dy2 = - Fr/M*(dy) - K/M*(y) + Fx
    return dy2  

# %% Programa principal:

dt = 1/fps
n = fps*Tf      

for i in range (n):
    dy2 = Segunda_derivada(Ti, Yi, Dyi)
    dy  = Dyi + dy2*dt
    y   = Yi  + dy*dt
    t   = Ti  + dt
    
    Dy += [dy]
    Y  += [y]
    T  += [t]
    
    Dyi, Yi, Ti = dy, y, t

X = [0]*n

d = 0.1*Yii

# %% Imprimir los datos:

Fig = plt.figure(constrained_layout = True)
Gs  = grid.GridSpec(2, 2, figure = Fig)
Fig.suptitle('Sistema Masa-resorte (Analisis numerico)')

plt.style.use('seaborn')

Ax1 = Fig.add_subplot(Gs[:, 0])
Ax1.set_title('Animacion')
Ax1.set_xlim(-1, 1)
Ax1.set_ylim(-1-d, 2+d)

Resorte1,  = Ax1.plot([], [], color = 'black', label = 'resorte')
Eje1,      = Ax1.plot([], [], '--', color = 'gray', label = 'Equilibrio')
Masa1,     = Ax1.plot([], [], 'o', color = 'black', label = 'Masa', markersize = 10)
Soporte1,  = Ax1.plot([], [], Color = 'black', linewidth = 5)
time_text  = Ax1.text(0.05, 0.9, '', transform = Ax1.transAxes)

Ax2 = Fig.add_subplot(Gs[0, 1])
Ax2.set_title('Solucion')
Ax2.set_xlabel('Tiempo [s]')
Ax2.set_ylabel('Posicion [m]')
Ax2.set_xlim(Tii, Tff)
Ax2.set_ylim(-Yii-d, Yii+d)

Masa2, = Ax2.plot([], [], 'o', color = 'black', label = 'Masa', markersize = 10)
Sol2,  = Ax2.plot([], [], color = 'black')
Eje2,  = Ax2.plot([], [], '--', color = 'gray') 

Ax3 = Fig.add_subplot(Gs[1, 1])
Ax3.set_title('Diagrama de fase')
Ax3.set_xlabel('Posicion [m]')
Ax3.set_ylabel('Velocidad [m/s]')
Ax3.set_xlim(-Yii-d, Yii+d)
Ax3.set_ylim(min(Dy)-d, max(Dy)+d)

Masa3, = Ax3.plot([], [], 'o', color = 'black', markersize = 10)
Eje3,  = Ax3.plot([], [], '--', color = 'gray') 
Sol3,  = Ax3.plot([], [], color = 'black')

plt.legend()

def Animacion(i):
    
    time_text.set_text('Tiempo: %.1fs' % (i*dt))
    
    Eje1.set_data([-1, 1], [0, 0])
    Resorte1.set_data([0, 0], [2, Y[i]])
    Masa1.set_data(X[i], Y[i])
    Soporte1.set_data([-0.2, 0.2], [2, 2])
    
    Masa2.set_data(T[i], Y[i])
    Sol2.set_data(T, Y)
    Eje2.set_data([Tii, Tff], [0, 0])
    
    Masa3.set_data(Y[i], Dy[i])
    Eje3.set_data([-Yii, Yii], [0, 0])
    Sol3.set_data(Y, Dy)
    
    return Eje1, Resorte1, Masa1, Masa2, Sol2, Eje2, Masa3, Eje3, Sol3

Anim = anim.FuncAnimation(Fig, Animacion, frames = n, interval = dt)
#Anim.save('Sistema masa-resorte.gif', fps=fps)
plt.show()

print('Fin del programa')
