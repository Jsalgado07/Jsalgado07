'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2021-10-25
'''

# %% Importación de librerías:

import numpy as np

# %% Definicion de constantes globales y espacions de memoria:

A = [[1, 3, 5, 5], 
     [5, 8, 3, 7], 
     [4, 6, 7, 1], 
     [8, 2, 6, 3]]

n = len(A)    
    
# %% Definición de funciones:

def Descomposicion_LU(A):
    
    A = np.array(A)
    L = np.eye(n, dtype=float)
    U = np.array(A, dtype=float)
    
    for k in range(n):
        U1 = np.array([f[:] for f in U])
        for i in range(k+1, n):
            for j in range(n):
                p = U[k,k]
                U1[i,j] += -U[i,k]*U[k,j]/p
                if j == k:
                    L[i,j] = U[i,k]/p
        U = U1
    
    return L, U

# %% Programa principal:

L, U = Descomposicion_LU(A)

# %% Imprimir los datos:

print('La matriz L es:\n',L )
print('\nLa matriz U es:\n', U)