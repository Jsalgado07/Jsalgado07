'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2021-??-??
'''

# %% Importación de librerías:

import numpy as np

# %% Definicion de constantes globales y espacions de memoria:

A = [[  1.  ,   0.  ,   0.  ,   0.  ,   0.  ,   0.  ,   0.  ,   0.  , 0.  ],
     [  9.  ,  -9.  ,   0.  ,   1.  ,  -1.  ,   0.  ,   0.  ,   0.  , 0.  ],
     [  0.  ,  14.  , -14.  ,   0.  ,   1.  ,  -1.  ,   0.  ,   0.  , 0.  ],
     [  9.  ,   0.  ,   0.  ,   3.  ,   0.  ,   0.  ,   1.  ,   0.  , 0.  ],
     [ 20.25,   0.  ,   0.  ,   4.5 ,   0.  ,   0.  ,   1.  ,   0.  , 0.  ],
     [  0.  ,  20.25,   0.  ,   0.  ,   4.5 ,   0.  ,   0.  ,   1.  , 0.  ],
     [  0.  ,  49.  ,   0.  ,   0.  ,   7.  ,   0.  ,   0.  ,   1.  , 0.  ],   
     [  0.  ,   0.  ,  49.  ,   0.  ,   0.  ,   7.  ,   0.  ,   0.  , 1.  ],
     [  0.  ,   0.  ,  81.  ,   0.  ,   0.  ,   9.  ,   0.  ,   0.  , 1.  ]]

B = [0, 0, 0, 2.5, 1.0, 1.0, 2.5, 2.5, 0.5]
    

# %% Definición de funciones:

def np_gauss_seidel(A, B):
    '''
        Solución de un sistema AX=B, donde:
        A: coeficientes constantes, se ingresa como una lista de listas.
        X: incógnitas
        B: constantes, se ingresa como una lista.
        Se usa el método iterativo de Gauss-Seidel con numpy sin considerar
        mejoramiento de la convergencia.
    '''
    A = np.array(A)
    B = np.array(B)
    n = len(A)       # Tamaño del sistema.
    
    # Se definen las matrices constantes del método.
    D = np.diag(np.diag(A))
    Dinv = np.diag(1/np.diag(A))
    T = A-D
    # Se define X0, para la primera iteración.
    X0 = np.zeros(n)

    toler = 0.0001
    paso = 0

    while True:
        X = np.array([X0[f] for f in range(n)])
        for i in range(n):
            x_i = Dinv[i, i]*(B[i] - T[i, :]@X0)  
            X0[i] = x_i
        paso += 1
        # Criterio de convergencia
        dis_puntos = sum((X0-X)**2)**0.5
        if dis_puntos < toler:
            print(f"Se hicieron {paso} iteraciones completas.")
            break

        # Criterio de divergencia
        if paso == 1000000:
            X0 = 'No converge'
            break
    X = X0
    return X


# %% Programa principal:

X = np.linalg.solve(A, B)
print (X)

# %% Imprimir los datos:



