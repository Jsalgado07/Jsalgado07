'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-02-22
'''


# %% Importación de librerías:

import matplotlib.pyplot as plt
from numpy import pi, sin, cos, linspace


# %% Definicion de constantes globales y espacions de memoria:

v0     = 2.34
theta0 = linspace(0, 2*pi, 100)    

ini = {"v0"    : v0,
       "theta0": theta0}

g = 9.8


# %% Definición de funciones:

def h_max(ini:dict):
    
    v = ini["v0"]
    theta = ini["theta0"]
    
    h = (v*sin(theta))**2/(2*g) 
    
    return h


# %% Programa principal:

high = h_max(ini)


# %% Imprimir los datos:

fig = plt.figure(figsize = (8, 4))
ax  = fig.add_subplot()

ax.plot(theta0, high) 
ax.set_title("Grafica de la altura en funcion del tiempo para un lanzamiento parabolico")
ax.set_xlabel("Angulo inicial de disparo")
ax.set_ylabel("Altura maxima del cuerpo")

plt.grid()
plt.show()

plt.savefig("Grafica.pdf", format = "pdf")
