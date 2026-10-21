'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-MM-DD
'''

'''
Graficamos la solucion analitica para la densidad de probabilidad inical
del spinor con ayuda de las funciones A(x, 0) y B(x, 0) segun se calculan en 
el articulo seguido.
'''

# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt

from numpy import cosh, sinh
from matplotlib import rc


# %% Definicion de constantes globales y espacions de memoria:

m = 1.0                     # Masa.
ω = 0.3                     # frecuencia.
κ = 1.0                     # Termino no lineal
β = (m**2 - ω**2)**0.5      # Constante del metodo.
g = 1.0                     # cosntante de la ecuacion.

i = 1j                      # Unidad imaginaria.


# %% Definición de funciones:

def A_0(x):
    
    '''
    Funcion solucion analitica de la condicion inicial para A(x, 0)
    la primera componente del espinor.
    '''
    
    A = ((((m + ω)*cosh(κ*β*x)**2)/(m + ω*cosh(2*κ*β*x)))**0.5*
         (((κ + 1)*β**2)/(g**2*(m + ω*cosh(2*κ*β*x))))**(1/(2*κ))) 
    
    return A


def B_0(x):
    
    '''
    Funcion solucion analitica de la condicion inicial para B(x, 0)
    la segunda componente del espinor.
    '''
    
    B = ((((m - ω)*sinh(κ*β*x)**2)/(m + ω*cosh(2*κ*β*x)))**0.5*
         (((κ + 1)*β**2)/(g**2*(m + ω*cosh(2*κ*β*x))))**(1/(2*κ)))
    return B


def ψ(x, t):
    
    '''
    Magnitud del espinor |ψ(x, t)|^2 donde definimos
    ψ(x, t) = [A(x, t) iB](x, t).
    '''

    A = A_0(x)   
    B = B_0(x)  

    ψ = A*A.conjugate() + B*B.conjugate()
    
    return ψ.real


# %% Programa principal:

X = np.linspace(-20, 80, 1000)      # Espacio de solucion espacial.
ψ = ψ(X, 0)                         # Definimos la magnitud del espinor.


# %% Imprimir los datos:
    
rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True) 

Fig = plt.figure(figsize = (8, 6))
Ax  = Fig.add_subplot()  

Ax.plot(X, ψ, color = '#5F084C')

Ax.set_xlabel(r'$x$', fontsize = 20)
Ax.set_ylabel(r'$|\Psi(x, 0)|^2 = |A(x, 0)|^2 + |B(x, 0)|^2$', fontsize = 20)

Ax.set_xlim(-20, 20)

plt.show()

