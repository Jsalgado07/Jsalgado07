'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2021-??-??

A partir de las ecuaciones de movimiento de dos particulas animar este movimiento.

'''

# %% Importación de librerías:

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import sin, cos, pi

# %% Definicion de constantes globales y espacions de memoria:

G = 9.8
M, m = 10, 1
k1, k2 = 1, 1
r = 1

x0, dx0, d2x0 = 0, 0, 0
a0, da0, d2a0 = pi/4, 0, 0

fps = 30
Time = 10
dt = 1/fps
n = fps*Time

X = [x0]
A = [a0]

# %% Definición de funciones:

def Ecuacion_x(x, dx, a, da, d2a):
    d2x = (-(k1+k2)*dx - k2*r*da*cos(a) - m*r*(d2a*cos(a)-da**2*sin(a)))/(m+M)
    return d2x

def Ecuacion_a(x, dx, d2x, a, da):
    d2a = (-k2*r*dx*cos(a) - k2*r**2*da - m*G*r*sin(a) - m*r*cos(a))/(m*r**2)
    return d2a

# %% Programa principal:    

for i in range(n):
    
    d2x = Ecuacion_x(x0, dx0, a0, da0, d2a0)
    d2a = Ecuacion_a(x0, dx0, d2x0, a0, da0)
    
    dx = dx0 + dt*d2x0
    da = da0 + dt*d2a0
    
    x = x0 + dt*dx0
    a = a0 + dt*da0 
    
    X.append(x)
    A.append(a)
    
    x0, dx0, d2x0 = x, dx, d2x
    a0, da0, d2a0 = a, da, d2a

X1 = X
Y1 = [0]*(n+1)  

X2, Y2 = [], []
for i in range(n+1):
    x2 = X1[i] + sin(A[i])
    y2 = Y1[i] - cos(A[i])
    
    X2.append(x2)
    Y2.append(y2)

# %% Imprimir los datos:

Fig = plt.figure()
plt.style.use('dark_background')
xx = Fig.add_subplot(xlim=(-2, 2), ylim=(-2, 1))

line, = xx.plot([], [], 'o-', lw=2)
barra, = xx.plot([], [])
#time_template = 'Tiempo = %.1fs'
time_text = xx.text(0.05, 0.9, '', transform=xx.transAxes)

def Animacion(i):
    
    Coord_x = [X1[i], X2[i]]
    Coord_y = [Y1[i], Y2[i]]
    
    x = [-2, 2]
    y = [0, 0]
    
    time_text.set_text('Tiempo: %.1fs' % (i*dt))
    barra.set_data(x, y)
    line.set_data(Coord_x, Coord_y)
    return line, barra

anim = animation.FuncAnimation(Fig, Animacion, frames = n, interval = 0.5)
#anim.save('Pendulo con friccion.gif', fps=fps)
plt.show()

print('Fin del programa')

