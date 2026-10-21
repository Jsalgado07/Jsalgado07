'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2021-11-05
'''

# %% Importación de librerías:

import numpy as np

# %% Definicion de constantes globales y espacions de memoria:
A = [[                      1.0000, 1.0000],
      [0.00000000000000000000000003, 3.0000]]

B = [ 1.0000, 2.00000000000000000000000001]

n = len(A)
m = len(A[0])

# %% Definición de funciones:
    
def  Metodo_Jacobi(A, B):
    
    A = np.array(A)
    B = np.array(B)
    
    D = np.diag(np.diag(A))
    D_inv = np.diag(1/np.diag(A))
    T = A - D
    X0 = np.zeros(n)
    
    Tol = 1e-14
    P = 0
    
    while True:
        TX0 = T@X0
        B_TX0 = B - TX0
        X1 = D_inv@B_TX0
        P += 1
        
        Dis_puntos = sum((X1-X0)**2)**0.5
        if Dis_puntos < Tol:
            print(f"Se hicieron {P} iteraciones.")
            break
        X0 = X1
        if P == 10000:
            X0 = 'No converge'
    
    X = X0 
    return X       
        
# %% Programa principal:

Sol = Metodo_Jacobi(A, B)

# %% Imprimir los datos:

print('La solucion del sistema es:\n', Sol)

