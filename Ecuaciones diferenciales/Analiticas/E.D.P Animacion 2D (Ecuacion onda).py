### IMPORTAR LIBRERIAS ###
from matplotlib import animation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import Animation

### CONDICIONES INICIALES ###
T = 14.4*10**4
P = 9.17
C = np.sqrt(T/P)
L = 5
E = 3
n = 20

### VALORES PARA LA ANIMACION ###
fps = 200
seg = 2
frn = fps * seg

### ESPACIO DE PLOTEO ###
fig = plt.figure()
xx = np.linspace(0, L, 100)
lines = plt.plot([])
line = lines[0]
plt.xlim(0, L)
plt.ylim(-E, E)
plt.xlabel('Posicion')
plt.ylabel('Altura')

### FUNCION EN SERIE DE FOURIER ###
def f1(x, t):
    f = 0
    for i in range(1, n):
        m = 2*i-1
        f += ((8*E)/(np.pi**2))*(((-1)**(i+1))/(m**2))*(np.sin((m*np.pi*x)/L))*(np.cos((C*m*np.pi*t/L)))
    return f 

### FUNCION ANIMADA ###
def Animacion(frames):
    t = frames/frn
    y = f1(xx, t)
    plt.title('Tiempo = {}'.format(t))
    line.set_data((xx, y))

### GRAFICAR Y GUARDAR ANIMACION ###
anim = Animation.FuncAnimation(fig, Animacion, frn, interval = 200/fps,)
anim.save('Solucion_Ecuacion_Onda.gif', fps=fps)
plt.show()


print('Fin del programa')