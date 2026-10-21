'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2022-01-26
'''


# %% Importación de librerías:

import sympy as sp
import numpy as np
from sympy import cos
from numpy import pi


# %% Definicion de constantes globales y espacions de memoria:

x = sp.symbols('x')
f = cos(x)

a = 0
b = pi/2

n = 10


# %% Programa principal:

F = sp.lambdify(x, f)                    # Argumento para evaluar la funcion
I0 = sp.integrate(f, (x, a, b))          # Valor real de la integral

d = (b-a)/n                              # Tamaño del intervalo en x                 # Espacio de evaluacion
     
Xi = np.arange(a+d, b, d*2)              # Evaluacion en puntos impares
Xp = np.arange(a+2*d, b, d*2)            # Evaluacion en puntos apres

I = ((d/3)*(F(a) + 4*sum(F(Xi))          # Area total de las parabolas
     + 2*sum(F(Xp) + F(b)))) 
e = round(float(abs((I-I0)/I0)), 4)      # Error del metodo


# %% Imprimir los datos:

print('\nMETODO DEL SIMPSON MULTIPLE\n')
print(f'El valor de la integral real es:\n {I0}')
print(f'El valor numerico de la integral con {n} particiones es:\n {I}')
print(f'El error del metodo es del {e*100}%.')