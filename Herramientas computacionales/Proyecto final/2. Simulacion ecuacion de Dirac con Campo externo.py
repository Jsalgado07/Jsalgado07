'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-06-15
'''

'''
Solucionamos las ecuaciones diferenciales parciales acopladas para  A(x,t) y
B(x,t) mediante el metodo de diferencias finitas para diferentes potenciales
V(x), dentro del regimen estable ω=0.9 e inestable ω = 0.3, con estas 
graficamos la densidad de probabilidad para el espinor Ψ(x, t) en diferentes 
tiempos.

(El metodo resulta muy sensible a la escogenca del parametro ω, las constantes
 del potencial V1 y V2, los deltas dx y dt y el tiempo hasta el cual se quiere
 simular, tener precaucion con estos parametros y seguir los establecidos en 
 en trabajo teorico.)
'''


# %% Importación de librerías:

import matplotlib.pyplot as plt

from numpy import cosh, sinh, arange
from matplotlib import rc


# %% Definicion de constantes globales y espacions de memoria:


m = 1.0                     # Masa.
ω = 0.9                     # frecuencia (inestable ω = 0.3, estable ω=0.9).
κ = 1.0                     # Termino no lineal
β = (m**2 - ω**2)**0.5      # Constante del metodo.
g = 1.0                     # cosntante de la ecuacion.

i = 1j                      # Unidad imaginaria.

dt = 0.01                   # Delta de intervalos en t.
dx = 0.2                    # Delta de intervalos en x. (Segun el caso escoger
                            # dx = 0.2 y dx = 0.02)

V1 = 0.1                    # Constante para el potencial lineal.
V2 = 0.01                   # Constante para el potencial cuadratico.

C = ['#5F084C',             # Paleta de colores para las graficas. 
     '#472255', 
     '#2F3C5E', 
     '#185567', 
     '#006F71']


# %% Definición de funciones:

def A_0(x):
    
    '''
    Funcion solucion analitica de la condicion inicial para A(x, 0)
    la primera componente del espinor.
    '''
    
    A = ((((m + ω)*cosh(κ*β*x)**2)/(m + ω*cosh(2*κ*β*x)))**0.5*
         (((κ + 1)*β**2)/(g**2*(m + ω*cosh(2*κ*β*x))))**(1/(2*κ))) 
    
    return A


def B_0(x):
    
    '''
    Funcion solucion analitica de la condicion inicial para B(x, 0)
    la segunda componente del espinor.
    '''
    
    B = ((((m - ω)*sinh(κ*β*x)**2)/(m + ω*cosh(2*κ*β*x)))**0.5*
         (((κ + 1)*β**2)/(g**2*(m + ω*cosh(2*κ*β*x))))**(1/(2*κ)))
    return B


def V(x):
    
    '''
    Potencial de interaccion, se varia entre el termino V = V1*x y
    V = V2/2*(x+5)**2 segun sea el caso.
    '''
    
    V = V1*x
    
    return V


def Soluciones(t):

    '''
    Se seleccionan las condiciones iniciales A(x, 0) y B(x, 0) con las 
    funciones A_0 y B_0 y se itera su evolucion temporal mediante diferencias
    finitas hasta el tiempo t.
    '''    

    A = A_0(X) + 0.0j
    B = B_0(X) + 0.0j

    for n in range(int(t/dt)):
        for x in range(1, len(X)-1):

            f = A[x]*A[x].conjugate() - B[x]*B[x].conjugate()

            A[x] = A[x] + dt*i*(-(B[x+1]-B[x-1])/(2*dx) -
                                V(X[x])*A[x] - (f-m)*A[x])
            B[x] = B[x] + dt*i*((A[x+1]-A[x-1])/(2*dx) -
                                V(X[x])*B[x] + (f-m)*B[x])

    return A, B


def Soliton(t):

    '''
    Con las funciones A(x, t) y B(x, t) calculadas con la funcion
    solucion(x, t) calculamos la magnitud del spinor.
    '''    

    A, B = Soluciones(t)
    Ψ = []
    for k in range(len(A)):
        m = A[k]*A[k].conjugate() + B[k]*B[k].conjugate()
        Ψ += [m.real]

    return Ψ, A, B


# %% Programa principal:

X = arange(-50, 50, dx)        # Espacio de solucion espacial.


# %% Imprimir los datos:

rc('font', **{'family': 'serif', 'serif': ['Times New Roman']})
rc('text', usetex=True)

Fig = plt.figure(figsize=(8, 6))
Ax = Fig.add_subplot()

k = 0
C_m = []
for t in range(0, 20, 5):        #(Escoger con precaucion.)
    Ψ, A, B = Soliton(t)
    for j in range(0, len(Ψ)):
        if Ψ[j] == max(Ψ):
            C_m += [X[j]]

    Ax.plot(X, Ψ, label=f'$|\Psi(x, {t})|^2$', color=C[k])
    k += 1
    print(f'iteracion t = {t} realizada')

Ax.set_xlabel(r'$x$', size=20)
Ax.set_ylabel(r'$|\Psi(x, t)|^2 = |A(x, t)|^2 + |B(x, t)|^2$', size=20)
Ax.set_xlim(-15, 30)
Ax.set_ylim(-0.01, 0.25)

plt.legend(fontsize=15)
plt.show()
