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

F = sp.lambdify(x, f)                # Argumento para evaluar la funcion
I0 = sp.integrate(f, (x, a, b))      # Valor real de la integral

d = (b-a)/n                          # Tamaño del intervalo en x
X = np.linspace(a, b, n)             # Espacio de evaluacion
 
Areas = (b-a)*(F(a) + 2*sum(F(X)) + F(b))/

                                       # Areas de los trapecios  
I = sum(Areas)                         # valor del area total
e = (float(abs((I-I0)/I0)), 4)         # Error del metodo


# %% Imprimir los datos:

print('\nMETODO DEL TRAPECIO\n')
print(f'El valor de la integral real es:\n {I0}')
print(f'El valor numerico de la integral con {n} particiones es:\n {I}')
print(f'El error del metodo es del {e*100}%.')

