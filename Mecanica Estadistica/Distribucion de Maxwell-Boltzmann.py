'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-10-18
'''


# %% Importación de librerías:


import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import pandas as pd

from matplotlib import rc
from numpy import pi, exp



# %% Definicion de constantes globales y espacions de memoria:




# %% Definición de funciones:

def progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', print_end="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        print_end   - Optional  : end character; default is '\r' to overwrite previous line (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    # Print New Line on Complete
    if iteration == total:
        print("\n")
        
        
def Dis_V(v, KT):
    
    P = (1/KT)*v*exp(-v**2/(2*KT)) 
    
    return P


def Dis_Vx(vx, KT):
    
    sigma = (KT)**0.5
    P = 1/(sigma*(2*pi))*exp(-vx**2/(2*sigma**2)) 
    
    return P



# %% Programa principal:

default_dpi=100
scale=2.0
posciciones= pd.read_csv('posiciones.txt', header=None)
velocidades= pd.read_csv('velocidades.txt', header=None)

posciciones=posciciones.iloc[:,:-1]
velocidades=velocidades.iloc[:,:-1]	


posciciones_x = posciciones.iloc[:, ::2]
posciciones_y = posciciones.iloc[:, 1::2]

velocidades_x = velocidades.iloc[:, ::2]
velocidades_y = velocidades.iloc[:, 1::2]


x=posciciones_x.to_numpy()
y=posciciones_y.to_numpy()
vel_x=velocidades_x.to_numpy()
vel_y=velocidades_y.to_numpy()

# print(x.transpose().shape)
# print(vel_x.transpose().shape)

N = x.shape[1]

r = 25

fps = 30
q=1/fps
t_max = 5

dt = 0.1
Frames = x.shape[0]

xi = np.zeros(N)
yi = np.zeros(N)
vxi = np.zeros(N)
vyi = np.zeros(N)

X = np.zeros((N, Frames))
Y = np.zeros((N, Frames))
# print(X.shape)

X= x.transpose()
Y= y.transpose()

Vel = np.zeros((len(vel_x), len(vel_x[0])))

for i in range(0, len(vel_x)):
    for j in range(0, len(vel_x[0])):        

        Vel[i, j] = (vel_x[i, j]**2 + vel_y[i, j]**2)**0.5

print('Desviación estandar', np.std(vel_x[146]))
print('Valor medio', np.mean(Vel[146]))


# %% Imprimir los datos: Simulación

# rc('font',**{'family':'serif','serif':['Times New Roman']})
# rc('text', usetex=True) 

# Fig = plt.figure(figsize = (8, 8), dpi = default_dpi*scale, 
#                   facecolor = '#0e1d3a')

# Ax = Fig.add_subplot()

# lim=300
# Ax.set_xlim(-10, lim+10)
# Ax.set_ylim(-10, lim+10)
# Ax.set_facecolor('#0e1d3a')

# Ax.plot([lim, lim, 0, 0, lim], [lim, 0, 0, lim, lim], color = 'black')
# Masas, = Ax.plot([], [], 'o', color = '#f79324', markersize = 15)

# Ax.set_xticks([])      
# Ax.set_yticks([])


# def Animacion(i):
        
#     Masas.set_data(X[:,i], Y[:,i])
#     Ax.set_title(f'Timer = {round((i/Frames)*t_max, 1)} seg', fontsize = 25,
#                   color = 'white')
#     progress_bar(i,Frames)
#     #make a progress bar using i and Frames here

#     return Masas

# Anim = anim.FuncAnimation(Fig, Animacion, frames = Frames, interval = 1000/fps)
# Anim.save("atomos.gif", fps=fps)
# plt.show()


# %% Imprimir los datos: (Histogramas)

fig = plt.figure(figsize = (8, 8), dpi = default_dpi*scale, 
                  facecolor = '#0e1d3a')

ax = fig.add_subplot()

velx = vel_x.transpose()
vely = vel_y.transpose()

xx = np.linspace(-30, 30, 1000)

def update_h(num):
    
    ax.clear()
    ax.set_ylim(0, 30)
    ax.set_xlim(-30, 30)
    ax.hist(vel_x[num], bins=40, color = '#b23273')
    ax.set_title(f'Timer = {round((num/Frames)*t_max, 1)} seg', color = 'w',
                  fontsize = 25)
    ax.plot(xx, Dis_Vx(xx, 50.11), 'w', lw = 3)
    ax.set_facecolor('#0e1d3a')
    ax.set_xlabel(r'$v_x$', color = 'w', fontsize = 25)
    ax.set_ylabel('Distribucion de probabilidad', color = 'w', fontsize = 25)

animation = anim.FuncAnimation(fig, update_h, frames=vel_x.shape[0], interval=100)
animation.save("hist.gif", fps=fps)
plt.show()

# print('Fin del programa')


# %% Imprimir los datos: (Histogramas)

# fig = plt.figure(figsize = (8, 8), dpi = default_dpi*scale, 
#                   facecolor = '#0e1d3a')

# ax = fig.add_subplot()

# velx = vel_x.transpose()
# vely = vel_y.transpose()

# # vel_x = np.array(vel_x)
# # vel_y = np.array(vel_y)

# Vel = np.zeros((len(vel_x), len(vel_x[0])))

# for i in range(0, len(vel_x)):
#     for j in range(0, len(vel_x[0])):        

#         Vel[i, j] = (vel_x[i, j]**2 + vel_y[i, j]**2)**0.5

# xx = np.linspace(0, 100, 1000)

# def update_h(num):
    
#     ax.clear()
#     ax.set_ylim(0, 20)
#     ax.set_xlim(0, 100)
#     ax.hist(Vel[num], bins=40, color = '#df5926')
#     ax.set_title(f'Timer = {round((num/Frames)*t_max, 1)} seg', color = 'w',
#                   fontsize = 25)
#     ax.plot(xx, 0.8*Dis_V(xx, 600), 'w', lw = 3)
#     ax.set_facecolor('#0e1d3a')
#     ax.set_xlabel(r'$v$', color = 'w', fontsize = 25)
#     ax.set_ylabel('Distribucion de probabilidad', color = 'w', fontsize = 25)

# animation = anim.FuncAnimation(fig, update_h, frames=vel_x.shape[0], interval=100)
# animation.save("hist2.gif", fps=fps)

# plt.show()

# print('Fin del programa')

