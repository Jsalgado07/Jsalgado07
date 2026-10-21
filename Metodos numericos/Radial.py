'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2022-11-04
'''
'''
Se usara este codigo para generar las variables del cogido 7.5
    
'''

# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt

from numpy import exp
from numpy import linalg as la


# %% Definicion de constantes globales y espacions de memoria:

N = 4                            # Particiones internas del intervalo.

a = 0                            # Limite inferior.
b = 50                           # Limite superior.

Ri = 0                           # Condiciones de contorno.
Rf = 0                           # Condiciones de contorno. 

a0 = 1                           # Radio de Borh.
n  = 4                           # Numero cuantico principal.
l  = 1                           # Numero cuantico azumutal. 

dr = (b-a)/(N+1)                 # Longuitud entre intervalo.

r = np.linspace(a, b, N+2)       # Valores para la solucion discreta.


# %% Definición de funciones:
      
def Ecuacion(i):
    '''
    Genera los coeficientes de la ecuacion i-esima como un vector para
    agregarla a la matriz de coeficientes    
    '''
    
    C = [0]*(N)                         # Generamos un vector con solo ceros.
    j = i+2
    
    if i == 0:                          
        C[i]   = (-2*r[j]**2/(dr**2) + 2*r[j]/(dr) + 2*r[j]/(a0) - 
                  r[j]**2/((a0*n)**2) - l*(l+1))  
        C[i+1] = r[j]**2/(dr**2)
        
    elif i == N-1:
        C[i]   = (-2*r[j]**2/(dr**2) + 2*r[j]/(dr) + 2*r[j]/(a0) - 
                  r[j]**2/((a0*n)**2) - l*(l+1))
        C[i-1] = r[j]**2/(dr**2) - 2*r[j]/(dr)
        
    else:
        C[i]   = (-2*r[j]**2/(dr**2) + 2*r[j]/(dr) + 2*r[j]/(a0) - 
                  r[j]**2/((a0*n)**2) - l*(l+1))        
        C[i+1] = r[j]**2/(dr**2)
        C[i-1] = r[j]**2/(dr**2) - 2*r[j]/(dr)
        
    return C


def Solucion(r):
    '''
    Expresion para la solucion analitica con n = 2 y l = 0.
    '''

    R = (1/(65*5**(1/2)))*(a0**(-3/2))*(1 - r/(12*a0))*(r/a0)**2*exp(-r/(4*a0))

    return R


# %% Programa principal:

# Calculo de los puntos internos:

M = []                    # Espacio de memoria para la matriz de coeficientes.

B = [0]*N                 # Vector nulo. 

for j in range(0, N):       # Recorro toda las filas agregando sus componentes.    
        Aj = Ecuacion(j)    # Se saca la ecuacion de la funcion.
        M += [Aj]           # Se agrega la ecuacion a la matriz.

M = np.array(M)             # Se escribe la matriz como un array en numpu 

M[-1, -2] = 0               # Haciendo 1 la ultima variable variable. 
B[-1] = M[-1, -1]/10


R_int = la.solve(M, B)          # Solucion del sistema para los puntos internos.


# Solucion entera:

R = [0]*(N+2)   
for i in range(0, N+2):     # Se agregan los bordes a la solucion.
    if i == 0:
        R[0] = Ri           # Se agrega el extremo menor.
    elif i == N+1:
        R[i] = Rf           # Se agrega el extremo mayor.
    else:
        R[i]= R_int[i-1]    # valores internos calculados al cuadrado.


# Normalizacion:
    
A = 0                              # Espacio de memoria para el area.
for k in range(0, N+1):            # Calculamos el area bajo la curva.   
    A += dr*(R[k]*r[k])**2         # Metodo del rectangulos.

R_nor = []                         # Espacio de memoria para la solucion normalizada.
for k in range(0, len(R)):         # Para cada componente de la solucion.
    R_nor += [R[k]/(A**0.5)]       # Se divide por la norma.


R_teo = np.array(Solucion(r))
R_exp = np.array(R_nor)

dif = abs(abs(R_exp)-abs(R_teo))/max(R_teo)

E = max(dif) 


# %% Imprimir los datos:

plt.style.use('default')    

Fig  = plt.figure()                  # Generar la figura.
Ax = Fig.add_subplot()               # Se genera unos ejes



rr = np.linspace(a, b, 1000)         # Se genera un espacio para la solucion analit.

Ax.plot(r, R_nor, color = '#F2668B', label='Aproximación')  # Solucion aproximada en rosado 
Ax.plot(rr, Solucion(rr), '#011F26', label='Teorica')


Ax.set_xlabel('1000 particiones'
              , fontsize = 17)                     # Titulo del eje x
Ax.set_ylabel('Funcion de onda radial -  R(r)'
              , fontsize = 17)                    # Titulo del eje y

Ax.grid()                              # Se pone cuadricula
plt.show()                             # Mostrar la figura.