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

x = sp.symbols('x')    # Variable simbolica
f = cos(x)             # Funcion que se quiere aproximar

a = 0                  # Limite de integracion inferior
b = pi/2               # Limite de integracion superior

n = 10                 # Cantidad de puntos intermedios 


# %% Programa principal:

F = sp.lambdify(x, f)           # Argumento para evaluar la funcion
I0 = sp.integrate(f, (x, a, b)) # Valor real de la integral

d = (b-a)/n                     # Tamaño del intervalo en x
Xe = np.linspace(a, b, n)       # Espacio de evaluacion
 
Areas = F(Xe)*d                 # Areas de los rectangulos  
I2 = sum(Areas)                 # valor del area total
E2 = float(abs((I2-I0)/I0))     # Error del metodo
E2 = round(E2, 4)

# %% Imprimir los datos:

print('\nMETODO DEL RECTANGULO\n')
print(f'El valor de la integral real es:\n {I0}')
print(f'El valor numerico de la integral con {n} particiones es:\n {I2}')
print(f'El error del metodo es del {E2*100}%.')

