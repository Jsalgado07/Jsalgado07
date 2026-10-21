'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-11-22
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt
    
from matplotlib import rc
from numpy import log


# %% Definicion de constantes globales y espacions de memoria:

E =  [-30, -10, 10, 30]
Ef = [-10, 10]

F = [log(2), log(2)]
B = [log(1), log(1), log(1), log(1)]
C = [log(1/6), log(1/2), log(1/2), log(1/6)]



# %% Imprimir los datos:

rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)

Fig = plt.figure(figsize = (8, 8), facecolor = '#0e1d3a')
Ax = Fig.add_subplot()

Ax.set_xlim(-35, 35)
Ax.set_ylim(-2, 2)
Ax.set_facecolor('#0e1d3a')

Ax.plot(E, B, '-o', color = '#b23273', label  = 'Bosones') 
Ax.plot(Ef, F, '-o', color = '#df5926', label = 'Fermiones') 
Ax.plot(E, C, '-o', color = '#f79324ff', label = 'Clasicas') 

# Ax.set_xlabel(r'Temperature $T$', fontsize = 15)
# Ax.set_ylabel(r'Average Energy $E/k_B$', fontsize = 15,)

plt.legend(fontsize = 15)
plt.grid()
plt.show()


