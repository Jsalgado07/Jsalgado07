'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-05-02
'''


# %% Importación de librerías:
    
import matplotlib.pyplot as plt
from numpy import zeros, pi, arange


# %% Definicion de constantes globales y espacion de memoria:

Delta_R = 0.1
Delta_Theta = 0.1

Theta_left = 0
Theta_righ = 100 
R_top = 100
    
R = arange(0, 2+Delta_R, Delta_R)
Theta = arange(0, 2*pi/3+Delta_Theta, Delta_Theta)

Psi = zeros([len(R), len(Theta)])

n = 50


# %% Definición de funciones:

def Laplace(Psi):
    
    for i in range(1, len(R)-1):
        for j in range(1, len(Theta)-1):
            
            g = ((Psi[i+1,j] + Psi[i-1,j])/(2*Delta_R**2) + 
                 Psi[i+1, j]/(R[i]*Delta_R) + 
                 (Psi[i, j+1] + Psi[i, j-1])/(2*R[i]**2*Delta_Theta**2))
            
            Psi[i, j] = g/(1/(Delta_R**2) + 1/(Delta_R*R[i]) + 1/(R[i]**2*Delta_Theta**2))

    return Psi


# %% Programa principal:

Psi[-1, :].fill(R_top)
Psi[:, 0].fill(Theta_left)
Psi[:, -1].fill(Theta_righ)

for i in range(n):
    Psi = Laplace(Psi)


# %% Imprimir los datos:

Fig = plt.figure(figsize = (10, 6))    
Ax  = Fig.add_subplot(111, polar = True) 

ctf = Ax.contourf(Theta, R, Psi, 50, cmap="viridis")
plt.colorbar(ctf)
plt.axis([0, 2*pi/3, 0, 2])
plt.show()


