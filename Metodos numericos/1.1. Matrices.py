#IMPORTAR LIBRERIAS
import numpy as np
import sympy as sp

#DEFINIR MATRICES
M = np.array([[1, 0], 
              [0, 1]]) 
print('La matriz M es:')
print(M)

#Caracteristicas:
Dimension_M = M.shape
Filas_M = Dimension_M[0]
Columnas_M = Dimension_M[1]
print('La matriz M tiene dimencion:', Dimension_M)
print('La matriz M tiene columnas:', Columnas_M)
print('La matriz M tiene filas:', Filas_M)

#Arreglos:
Unos = np.ones((3, 4))
print(Unos)
Ceros = np.zeros((5, 5))
print(Ceros)   
Identidad = np.identity((3))  #Cuadrada
print(Identidad)
Identidad_general = np.eye(3, 4)  #General mxn
print(Identidad_general)

#LLamado de elementos:
J = np.array([[1, 3, 5, 5], 
              [3, 4, 7, 9],
              [0, 2, 6, 7],
              [4, 6, 8, 2]])

j12 = J[2, 3]
print('El elemento fila 2 columna 2 es:', j12)
jf1 = J[0]
print('La fila 1 es:', jf1)
jc2 = J[:, 1]
print('La columna 2 es:', jc2) 

#MODIFICACION
C = np.array([[1, 3, 6, 7], 
              [4, 7, 8, 0], 
              [4, 9, 2, 1]])
C[2, 2] = 9
print(C)
C[1] = [1, 2, 3, 4]
print(C)
C[:, 0] = 0
print(C)

#OPERACIONES
M = np.array([[3, 5, 7],
              [4, 6, 2], 
              [2, 5, 1]])
N = np.array([[1, 5, 2],
              [4, 6, 2], 
              [4, 2, 1]])

Suma = N+M
print('La suma de las matrices m y N es: \n', Suma)
Resta = M-N
print('La resta de las matrices m y N es: ', Resta)
Producto_1 = np.matmul(N, M)
Producto_2 = M@N
print('El producto de las matrices M y N es: ', Producto_1)
print(Producto_2)
Determinante_M = np.linalg.det(M)
Determinante_N = np.linalg.det(N)
print('El determinante de M es', Determinante_M, ' Y el determinante de N es: ', Determinante_N)
Inversa = np.linalg.inv(M)
print('\n La inversa de la matriz M es: \n', Inversa)
Transpuesta = N.T
print('\n La trapuesta de la matriz N es:\n', Transpuesta)

u = np.array([80, 32, -64])
v = np.array([0.2, 0.08, 0.29])

P_Punto = np.dot(u, v)
print('\n El producto punto entre los vectores u y v es: \n', P_Punto)
P_Cruz = np.cross(u, v)
print('\n El producto cruz entre los vectores u y v es: \n', P_Cruz*10**7/(4*np.pi))