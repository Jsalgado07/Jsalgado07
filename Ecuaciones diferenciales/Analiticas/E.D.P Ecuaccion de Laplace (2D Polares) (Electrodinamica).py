'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-MM-DD
'''
'''
Potencial en interior de una esfera  V = 0 en su superficie con una varilla
en el eje z  con densidad de carga.
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt

from numpy import cos, pi, log


# %% Definicion de constantes globales y espacions de memoria:

ε = 1
R = 1
λ = 1


# %% Definición de funciones:

    
def Legendre(n, x):
    
    N = [0]*(n+1)
    N[n] = 1
            
    P = np.polynomial.legendre.Legendre(N, domain=None, window=None)

    return P(x)


def Φ(r, θ):
    
    Φ = -r**2*R/5 + (r/R)**2*(R**2/5 - R**3*log(R/r)) 
    
    for l in range(0, 20):
        if l != 2 and l%2 == 0: 
            Φ += -12*λ/(R*ε)*Legendre(l, cos(θ))*((-1/(l+3) + 1/(-l+2))
                                                *(r**2 - R**2*(r/R)**l))
    return Φ


# %% Programa principal:

R_list = np.linspace(0, R, 1000)
θ_list = np.linspace(0, 2*pi, 1000)

θ_list_p , R_list_p = np.meshgrid(θ_list, R_list)


# %% Imprimir los datos:

Fig = plt.figure(figsize = (10, 6))    
Ax  = Fig.add_subplot(111, polar = True) 

ctf = Ax.contourf(θ_list, R_list, Φ(R_list_p, θ_list_p), 50, cmap="viridis")
plt.colorbar(ctf)
plt.axis([0, 2*pi, 0, R])
plt.show()


