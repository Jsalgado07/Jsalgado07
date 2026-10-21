'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-06-14
'''

'''
Solucionamos la ecuacion diferencial para q(t) bajo el potencial lineal 
mediante el metodo de de Runge-Kutta y comparamos esta solucion con los 
centros de carga calculados en el codigo (2).
'''


# %% Importación de librerías:

import matplotlib.pyplot as plt

from scipy.misc import derivative as der
from numpy import cosh, sinh, arange
from matplotlib import rc
from scipy.integrate import quad as qu


# %% Definicion de constantes globales y espacions de memoria:

m = 1.0                          # Masa.
ω = 0.3                         # frecuencia.
κ = 1.0                         # Termino no lineal
β = (m**2 - ω**2)**0.5          # Constante del metodo.
g = 1.0                         # cosntante de la ecuacion.

i = 1j                          # Unidad imaginaria.

dt = 0.0001                     # Delta de intervalos en t.
dx = 0.02                       # Delta de intervalos en x.
    
V1 = 0.1                        # Constante para el potencial lineal.
Q = 1                           # Normalizacion del espinor.

q_0 = 0                         # Condicion inicial q(0).
dq_0 = 0                        # Condicion inicial dq(0)/dt.

C_m = [7.815970093361102e-12,   # Centros de carga calculados con el codigo 2.
       2.52000000000821,
       7.080000000008923,
       12.640000000009792,
       18.64000000001073]

C = ['#5F084C',                 # Paleta de colores para los centros de masa 
     '#472255', 
     '#2F3C5E', 
     '#185567', 
     '#006F71']


# %% Definición de funciones:

def A(x):
    
    '''
    Funcion solucion analitica de la condicion inicial para A(x, 0)
    la primera componente del espinor.
    '''
    
    A = ((((m + ω)*cosh(κ*β*x)**2)/(m + ω*cosh(2*κ*β*x)))**0.5*
         (((κ + 1)*β**2)/(g**2*(m + ω*cosh(2*κ*β*x))))**(1/(2*κ))) 
    
    return A


def B(x):
    
    '''
    Funcion solucion analitica de la condicion inicial para B(x, 0)
    la segunda componente del espinor.
    '''
    
    B = ((((m - ω)*sinh(κ*β*x)**2)/(m + ω*cosh(2*κ*β*x)))**0.5*
         (((κ + 1)*β**2)/(g**2*(m + ω*cosh(2*κ*β*x))))**(1/(2*κ)))
    return B


def Ec(t, q):
    
    '''
    Ecuacion diferencial para q(t) con el termino dq/dt despejado. 
    '''
    
    dq = (c1*t + c2)/((1 + (c1*t + c2)**2)**0.5)    
    
    return dq


def RungeKutta4(ti, tf, dt, q0):
        
    '''
    Se itera la solucion para q(t) a cuarto orden.    
    '''
    
    T = arange(ti, tf, dt)
    q = [q_0]
    
    for i in range(len(T)-1):       
        
        k1 = Ec(T[i], q[i])
        k2 = Ec(T[i] + dt/2, q[i] + dt*k1/2)
        k3 = Ec(T[i] + dt/2, q[i] + dt*k2/2)
        k4 = Ec(T[i] + dt, q[i] + dt*k3)
        
        q_p = q[i] + 1/6*(k1 + 2*k2 + 2*k3 + k4)*dt
        q  += [q_p]    
    
    return T, q


# %% Programa principal:

I, err = qu(lambda x: A(x)*der(B, x, dx=1e-6) - B(x)*der(A, x, dx=1e-6),
            -20, 20)

M = I + ω*Q

c1 = V1*Q/M
c2 = dq_0/((1-dq_0**2)**0.5)    


T, q = RungeKutta4(0, 30+dt, dt, q_0)

X = arange(-20, 80, dx)


# %% Imprimir los datos:

rc('font',**{'family':'serif','serif':['Times New Roman']})
rc('text', usetex=True)     

Fig = plt.figure(figsize = (8, 6))
Ax  = Fig.add_subplot()
Ax.plot(T, q, '-', color = C[0], label='Solucion numerica $q(t)$')

k = 0
for j in range(0, 21, 5):
    Ax.plot(T[int(j/dt)], C_m[k], 'o', color = C[k],
            label = f'Centro carga $|\Psi(x, {j})|^2$')
    k += 1

Ax.set_xlabel('$t$', fontsize = 15)
Ax.set_xlim(0, 25)
plt.legend(fontsize = 15)
plt.show()
