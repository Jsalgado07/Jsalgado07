'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-10-15
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr

from matplotlib import rc
from numpy import exp, pi, tanh, sinh



# %% Definicion de constantes globales y espacions de memoria:

N = 10000

B = 10
K = 1
u = 2


# %% Definición de funciones:

# def State():
    
def Uz_mean(T):
    
    mean = u*(1/tanh(u*B/(K*T)) - K*T/(u*B))
    
    return mean


def uz_mean(T):
    
    S1 = 0
    S2 = 0    

    for i in range(0, N):
        
        uz = npr.uniform(-u, u)
        S1 += uz*exp(B*uz/(K*T))
        S2 += exp(B*uz/(K*T))

    uz_mean = (S1/S2)
    
    return uz_mean


# %% Programa principal:

x = np.arange(0.1, 4, 0.1)

U_teo = Uz_mean(u*B/(K*x))
U_sim = uz_mean(u*B/(K*x))


# %% Imprimir los datos:

rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)        

Fig = plt.figure(figsize = (8, 6), facecolor = '#0e1d3a')
Ax = Fig.add_subplot()

Ax.plot(x, U_teo,'--', label = 'Teorica', color = 'white', lw = 4)
Ax.plot(x, U_sim, label = 'Simulación', color = '#5F084C', lw = 4)

Ax.set_xlabel(r'$x= \frac{uB}{k_BT}$', fontsize = 15)
Ax.set_ylabel(r'$<u_z>$', fontsize = 15)
Ax.set_facecolor('#0e1d3a')

plt.legend(fontsize = 15)
plt.show()
plt.grid()



