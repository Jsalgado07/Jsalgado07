'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-MM-DD
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from numpy import pi, cos, linspace


# %% Definicion de constantes globales y espacions de memoria:

Alpha = 0.0
Beta  = 4*pi**2
Gamma = 30*pi**2
Delta = 0.1*pi
Omega = 2*pi



# %% Definición de funciones:

def Func(t, y):
    
    R1 = y[1]
    R2 = -Delta*y[1] - Alpha*y[0] - Beta*y[0]**3 + Gamma*cos(Omega*t)
    
    return [R1, R2]


# %% Programa principal:

y0     = [1, 0]
t_span = [0, 10]


Sol = solve_ivp(Func, t_span, y0, t_eval = linspace(t_span[0], t_span[1], 1000))

# %% Imprimir los datos:

Fig = plt.figure(figsize = (8, 6))
Ax  = Fig.add_subplot()

Ax.plot(Sol.t, Sol.y[0], 'r', label  = '$X(t)$')


