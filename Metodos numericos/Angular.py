'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2022-11-04
'''
'''
Se usara este cogigo para generar variables del codigo 7.5
    
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt

from numpy import pi, sin, cos
from numpy import linalg as la


# %% Definicion de constantes globales y espacions de memoria:

N = 1000                          # Particiones internas del intervalo.

a = 0                            # Limite inferior.
b = pi                           # Limite superior.

Gi = 1                           # Condiciones de contorno.
Gf = -1                           # Condiciones de contorno. 

l  = 1                           # Numero cuantico azumutal. 

dg = (b-a)/(N+1)                 # Longuitud entre intervalo.

g = np.linspace(a, b, N+2)       # Valores para la solucion discreta.


# %% Definición de funciones:
      
def Ecuacion(i):
    '''
    Genera los coeficientes de la ecuacion i-esima como un vector para
    agregarla a la matriz de coeficientes    
    '''
    
    C = [0]*(N)                         # Generamos un vector con solo ceros.
    j = i+1
    
    if i == 0:                          
        C[i]   = (-2*sin(g[j])**2/(dg**2) + sin(g[j])*cos(g[j])/dg 
                  + l*(l+1)*sin(g[j])**2)         
        C[i+1] = sin(g[j])**2/(dg**2)
        
    elif i == N-1:
        C[i]   = (-2*sin(g[j])**2/(dg**2) + sin(g[j])*cos(g[j])/dg 
                  + l*(l+1)*sin(g[j])**2)         
        C[i-1] = sin(g[j])**2/(dg**2) - sin(g[j])*cos(g[j])/dg
        
    else:
        C[i]   = (-2*sin(g[j])**2/(dg**2) + sin(g[j])*cos(g[j])/dg 
                  + l*(l+1)*sin(g[j])**2)         
        C[i+1] = sin(g[j])**2/(dg**2)
        C[i-1] = sin(g[j])**2/(dg**2) - sin(g[j])*cos(g[j])/dg
        
    return C


def Solucion(g):
    '''
    Expresion para la solucion analitica con l = 2.
    '''

    G = (5/(16*pi))**(1/2)*(3*cos(g)**2 - 1)

    return G


# %% Programa principal:

# Calculo de los puntos internos:

M = []                    # Espacio de memoria para la matriz de coeficientes.
I = np.identity(N)        # Creamos una matriz identidad. 

B = [0]*N

for j in range(0, N):       # Recorro toda las filas agregando sus componentes.    
        Aj = Ecuacion(j)    # Se saca la ecuacion de la funcion.
        M += [Aj]           # Se agrega la ecuacion a la matriz.

M = np.array(M)             # Se escribe la matriz como un array en numpu 

M[0, 1] = 0                 # Haciendo 1 la primera variable. 
B[0] = M[0, 0] 

M[-1, -2] = 0               # Haciendo 1 laultima variable. 
B[-1] = -M[-1, -1] 
             


G_int = la.solve(M, B)          # Solucion del sistema para los puntos internos.

# Solucion entera:

G = [0]*(N+2)   
for i in range(0, N+2):     # Se agregan los bordes a la solucion.
    if i == 0:
        G[0] = Gi           # Se agrega el extremo menor.
    elif i == N+1:
        G[i] = Gf           # Se agrega el extremo mayor.
    else:
        G[i]= G_int[i-1]    # valores internos calculados al cuadrado.


# Normalizacion:
    
A = 0                                  # Espacio de memoria para el area.
for k in range(0, N+2):                # Calculamos el area bajo la curva.   
    A += dg*G[k]**2*sin(g[k])          # Metodo del trapecio.

G_nor = []                  # Espacio de memoria para la solucion normalizada.
for k in range(0, len(G)):         # Para cada componente de la solucion.
    G_nor += [G[k]/((2*pi*A)**0.5)]       # Se divide por la norma.


# %% Imprimir los datos:

plt.style.use('default')    

Fig  = plt.figure()                  # Generar la figura.
Ax = Fig.add_subplot()               # Se genera unos ejes

gg = np.linspace(a, b, 1000)     # Se genera un espacio para la solucion analit.


Ax.plot(g, G_nor, '--', color = 'red')  # Solucion aproximada en rojo punteado 
Ax.plot(gg, Solucion(gg), 'black')     # Solucion analitica en negro.

Ax.set_xlabel('theta')                 # Titulo del eje x
Ax.set_ylabel('THETA(theta)')          # Titulo del eje y
Ax.grid()                              # Se pone cuadricula

plt.show()                             # Mostrar la figura.
