'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2022-11-04
'''
'''
Se plantea resolver la  ecuacion de la forma:
    
    -u'' + 2*sig^2*sec^2(sig*x)u = 4*sig^2*cos^2(sig*x)
    u(0) = 1
    u(1) = -sin^2(sig)
    
en el intervalo 0<x<1 con sig = 3/2 por el metodo de diferencias finitas con 
N = 8 particiones.
    
'''

# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt

from numpy import sin, cos, tan
from numpy import linalg as la


# %% Definicion de constantes globales y espacions de memoria:

N = (2**7) - 1               # Particiones del intervalo.

a = 0                        # Limite inferior.
b = 1                        # Limite superior.

sig = 3/2                    # Constante de la ecuacion.
u0  = 1                      # Condicion de contorno 1.
u1  = -sin(sig)**2           # Condicion de contornno 2.

dx = (b-a)/(N+1)             # Longuitud entre intervalo.

X = np.linspace(0, 1, N+2)   # Valores para la solucion exacta.

# %% Definición de funciones:
    
def Gauss_seidel(A, B):
    '''
        Solución de un sistema AX=B, donde:
        A: coeficientes constantes, se ingresa como una lista de listas.
        X: incógnitas
        B: constantes, se ingresa como una lista.
        Se usa el método iterativo de Gauss-Seidel con numpy sin considerar mejoramiento de la
        convergencia.
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
    
    
def Ecuacion(i):
    '''
    Genera los coeficientes de la ecuacion i-esima como un vector para
    agregarla a la matriz de coeficientes    
    '''
    
    C = [0]*(N+2)                 # Generamos un vector con solo ceros.

    if i == 0 or i == N+1:        # La primera y ultima ecuacion solo tienen 
        C[i] = 1                  # un coeficiente.
    
    else:       
        C[i]   = (2/dx**2 +       # Coeficientes de la ecuacion discretizada.
                  2*(sig/cos(X[i]*sig))**2)    
        C[i+1] = -1/dx**2
        C[i-1] = -1/dx**2
    
    return C


def Independiente(i):
    '''
    Se genera el valor para el los coeficientes constantes de la ecuacion
    dados por la ecuacion diferencial discretizada.
    '''

    if i == 0:          # EL primero es la conducion de frontera
        I = u0

    elif i == N+1:      # El ultimo es la condicion de frontera.
        I = u1
    
    else:                              # Los demas coeficientes estan dados 
        I = 4*(sig*cos(sig*X[i]))**2   # formula que se muestra

    return I 


def Solucion(x):
    '''
    Expresion para la solucion anaitica de la ecuacion diferencial planteada.
    '''

    u = cos(sig*x)**2 - tan(sig*x)/tan(sig)

    return u


# %% Programa principal:

M = []                    # Espacio de memoria para la matriz de coeficientes.
B = []                    # Espacio de memoria para el vector de term. indepen.

for j in range(0, N+2):   # Recorro toda las filas agregando sus componentes.    
        Aj = Ecuacion(j)        # Se saca la ecuacion de la funcion.
        Bj = Independiente(j)   # Se saca el coeficiente de la funcion.

        B += [Bj]               # Se agrega la ecuacion a la matriz. 
        M += [Aj]               # Se agrega el coeficiente al vector.

U = Gauss_seidel(M, B)          # Se soluciona el sistema MU = B.

xx = np.linspace(0, 1, 1000)    # Se genera un espacio para la solucion analit.

E = max(abs(Solucion(X)-U))     # Se calcula el error maximo del metodo.

print('Error = ', E)            # Se muestra el error maximo.
print('h = ', dx)               # Se muestra el paso.


# %% Imprimir los datos:

Fig  = plt.figure()             # Generar la figura.
Ax = Fig.add_subplot()          # Se genera unos ejes

Ax.plot(X, U, '--', color = 'red')   # Solucion aproximada en rojo punteado 
Ax.plot(xx, Solucion(xx), 'black')   #Solucion analitica en negro.

Ax.set_xlabel('x')                   # Titulo del eje x
Ax.set_ylabel('U(x)')                # Titulo del eje y
Ax.grid()                            # Se pone cuadricula

plt.show()                           # Mostrar la 



