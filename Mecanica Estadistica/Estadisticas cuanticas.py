'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-MM-DD
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt

from numpy import sinh, cosh
from matplotlib import rc


# %% Definicion de constantes globales y espacions de memoria:

E_min = -30
E_max = 10



# %% Definición de funciones:

def Bosones(T):
    
    f = -(10*sinh(10/T)+30*sinh(30/T))/(cosh(10/T) + cosh(30/T))
    
    return f
    

def Fermiones(T):
    
    f = -10*sinh(10/T)/cosh(10/T)
    
    return f


def Clasicas(T):
    
    f = -30*sinh(10/T)/cosh(10/T)
    return f

# %% Programa principal:

tt = np.linspace(0, 80, 1000)


# %% Imprimir los datos:

rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)

Fig = plt.figure(figsize = (8, 8), facecolor = '#0e1d3a')
Ax = Fig.add_subplot()

Ax.set_xlim(0, 80)
Ax.set_ylim(-30, 10)
Ax.set_facecolor('#0e1d3a')

Ax.plot(tt, Bosones(tt), color = '#b23273', label  = 'Bosones', 
        lw = '5') 
Ax.plot(tt, Fermiones(tt), color = '#df5926',label = 'Fermiones', 
        lw = '5') 
Ax.plot(tt, Clasicas(tt), color = '#f79324ff', label  = 'Clasicas', 
        lw = '5') 

Ax.set_xlabel(r'Temperature $T$', fontsize = 15)
Ax.set_ylabel(r'Average Energy $E/k_B$', fontsize = 15)

plt.legend(fontsize = 15)
plt.grid()
plt.show()


