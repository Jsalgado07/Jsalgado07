'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2022-11-13
'''
'''
Se plantea resolver el sigiente problema de valores propios:
    
    -Y''(x) = L*Y(x)
    Y(0) = 0
    Y(1) = 0
    
En el intervalo 0<x<b por el metodo de diferencias finitas. generalizado para
cualquier valor propio conocido y graficar la solucion normalizada y eleveada
al cuadrado.
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt

from numpy import sin, pi
from numpy import linalg as la


# %% Definicion de constantes globales y espacions de memoria:

N = 4                            # Particiones internas del intervalo.

a = 0                            # Limite inferior.
b = 1                            # Limite superior.

Yi = 0                           # Condicion de contorno nulas.
Yf = 0

n = 3                            # Armonico deseado.
L = (n*pi/b)**2                  # Valor propio. 

dx = (b-a)/(N+2)                 # Longuitud entre intervalo.

X = np.linspace(a, b, N+2)       # Valores para la solucion discreta.


# %% Definición de funciones:
      
def Ecuacion(i):
    '''
    Genera los coeficientes de la ecuacion i-esima como un vector para
    agregarla a la matriz de coeficientes    
    '''
    
    C = [0]*(N)                         # Generamos un vector con solo ceros.

    if i == 0:                          #
        C[i]   =  2/(dx**2) 
        C[i+1] = -1/(dx**2)
        
    elif i == N-1:
        C[i]   =  2/(dx**2)
        C[i-1] = -1/(dx**2)
        
    else:
        C[i]   =  2/(dx**2)        
        C[i+1] = -1/(dx**2)
        C[i-1] = -1/(dx**2)
        
    return C


def Solucion(x):
    '''
    Expresion para la solucion analitica de la ecuacion diferencial planteada.
    '''

    Y = (2/b)*sin(n*pi*x/b)**2

    return Y


# %% Programa principal:

# Calculo de los puntos internos:

M = []                    # Espacio de memoria para la matriz de coeficientes.
I = np.identity(N)        # Creamos una matriz identidad. 

B = [0]*N

for j in range(0, N):       # Recorro toda las filas agregando sus componentes.    
        Aj = Ecuacion(j)    # Se saca la ecuacion de la funcion.
        M += [Aj]           # Se agrega la ecuacion a la matriz.

M = np.array(M)             # Se escribe la matriz como un array en numpu


D = M - L*I                 # Le agregamos el valor propio a la matriz B. 

B[0] = D[0, 0]              # Asignamos la primera incognita como 1.
D[0, 1] = 0 


Y_int = la.solve(D, B)      # Solucion del sistema para los puntos internos.


# Solucion entera:

Y = [0]*(N+2)   
for i in range(0, N+2):     # Se agregan los bordes a la solucion.
    if i == 0:
        Y[0] = Yi           # Se agrega el extremo menor.
    elif i == N+1:
        Y[i] = Yf           # Se agrega el extremo mayor.
    else:
        Y[i]= Y_int[i-1]**2 # valores internos calculados al cuadrado.


# Normalizacion:
    
A = 0                       # Espacio de memoria para el area.
for k in range(0, N+1):     # Calculamos el area bajo la curva.
    A += dx*(Y[k])          # Metodo del trapecio.

Y_nor = []                  # Espacio de memoria para la solucion normalizada.
for k in range(0, len(Y)):  # Para cada componente de la solucion.
    Y_nor += [Y[k]/A]       # Se divide por la norma.


E = max(abs(Solucion(X)- Y_nor))   # Se calcula el error maximo del metodo.

print('Error = ', E)              # Se muestra el error maximo.
print('dx = ', dx)                # Se muestra el paso.


# %% Imprimir los datos:

Fig  = plt.figure()                  # Generar la figura.
Ax = Fig.add_subplot()               # Se genera unos ejes

xx = np.linspace(a, b, 1000)     # Se genera un espacio para la solucion analit.


Ax.plot(X, Y_nor, '--', color = 'red') # Solucion aproximada en rojo punteado 
Ax.plot(xx, Solucion(xx), 'black')     # Solucion analitica en negro.

Ax.set_xlabel('x')                     # Titulo del eje x
Ax.set_ylabel('Y(x)')                  # Titulo del eje y
Ax.grid()                              # Se pone cuadricula

plt.show()                             # Mostrar la figura.