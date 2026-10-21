'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2021-10-25
'''

# %% Importación de librerías:

import numpy as np

# %% Definicion de constantes globales y espacions de memoria:

A = [[1,  1, 1],
     [1,  2, 1],
     [2, -1, 1]]

B =  [0, 10, 4]
n = len(B)
    
# %% Definición de funciones:

def Metodo_Gauss_Jordan(A, B):

    A = np.array(A, dtype=float)
    B = np.array([B], dtype=float).T
    S = np.append(A, B, axis=1)
    sol = 0
    
    for j in range(n):
        
        Fj = S[j,:-1]               #Verificar fila
        Ver_F = np.isclose(Fj, 0)
        Sum_F = Ver_F.sum()
        
        Cj = S[:, j]                #Verificar Columnas
        Ver_C = np.isclose(Cj, 0)
        Sum_C = Ver_C.sum()
        
        if Sum_C == n or Sum_F == n:
            sol = 'El sistema es singular'
      
        else:                       #Pivoteo parcial
            R = S[j:,j:]
            Max_F = abs(R[:,:-1]).max(axis=1)
            Cj = abs(R[:,0])
            
            Div = Cj/(Max_F + 1e-14)
            Idx = np.where(Div == max(Div))[0][0] + j
            S1 = np.array([f[:] for f in S])
            S[j, :] = S1[Idx, :]
            S[Idx, :] = S1[j, :]
            
            P = S[j,j]              #Pivoteo
            S[j,:] = S[j,:]/P
            for i in range(n):
                if i != j:
                    S[i,:] = S[i,:] - S[i,j]*S[j,:]
            sol = S[:, -1]
   
    return list(sol)

# %% Programa principal:

Sol = Metodo_Gauss_Jordan(A, B)

# %% Imprimir los datos:

if Sol == 'El sistema es singular':
    print(Sol)
        
else:
    print('La solucion del sistema es:')
    for i in range(n):
        print(f"x{i+1}:", round(Sol[i], 3))     