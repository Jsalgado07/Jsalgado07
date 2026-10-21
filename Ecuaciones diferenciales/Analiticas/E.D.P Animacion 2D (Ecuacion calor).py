### IMPORTAR LIBRERIAS ###
from matplotlib import animation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import Animation, FuncAnimation

### CONDICIONES INICIALES ###
n = 20
d = 1.1*10**-2

### VALORES PARA LA ANIMACION ###
fps = 60
seg = 2
frn = fps * seg

### ESPACIO DE PLOTEO ###
fig = plt.figure()
xx = np.linspace(0,5,100)
lines = plt.plot([])
line = lines[0]
plt.xlim(0,5)
plt.ylim(-5,5)
plt.xlabel('Posicion')
plt.ylabel('Temperatura')

### FUNCION EN SERIE DE FOURIER ###
def f1(x, t):
    f = 0
    for i in range(1, n):
        m = 2*i-1
        f += ((40)/(np.pi**2))*(1/(m**2))*(np.cos((m*np.pi*x)/5))*(np.exp(-d*(m*np.pi/5)**2*t))
    return f

def f2(x, t):
    f = (-1/12) 
    for i in range(1, n):
       f += (2/5)*(((-1)**i)*(425/((i*np.pi)**2)-3750/((i*np.pi)**4))-350/((i*np.pi)**2)+3750/((i*np.pi)**4))*(np.cos(i*np.pi*x/5))*(np.exp(-d*(i*np.pi/5)**2*t))
    return f

### FUNCION ANIMADA ###
def Animacion(frames):
    t = frames
    y = f2(xx, t)
    plt.title('Tiempo = {}'.format(t))
    line.set_data((xx, y))

### GRAFICAR Y GUARDAR ANIMACION ###
anim = animation.FuncAnimation(fig, Animacion, frn, interval = 200/fps)
anim.save('Solucion_Ecuacion_Calor.gif', fps=fps)
plt.show()


print('Fin del programa')