'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-MM-DD
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt

# %% Definicion de constantes globales y espacions de memoria:

n = 1000000

det1, tr1 = [], []
det2, tr2 = [], []
det3, tr3 = [], []
det4, tr4 = [], []
det5, tr5 = [], []
det6, tr6 = [], []
det7, tr7 = [], []
det8, tr8 = [], []
det9, tr9 = [], []

e = 1e-6


# %% Definición de funciones:

def Matriz():
    
    M = np.random.random(size = (2, 2)) - np.random.random(size = (2, 2))
    det  = np.linalg.det(M)
    tr = np.trace(M)
    
    return tr, det


# %% Programa principal:

for i in range(n):
    
    x, y = Matriz()
    
    if y < -e:
        tr1  += [x]
        det1 += [y]

    elif x > 0 and y < x**2/4 - e and y > e:
        tr2  += [x]
        det2 += [y]
        
    elif x <= 0 and y < x**2/4 - e and y > e:
        tr3  += [x]
        det3 += [y]
        
    elif x > 0 and y > x**2/4 - e and y < x**2/4 + e:
        tr4  += [x]
        det4 += [y]
        
    elif x <= 0 and y > x**2/4 - e and y < x**2/4 + e:
        tr5  += [x]
        det5 += [y]
    
    elif abs(y) <= e and x <= e:     
        tr6  += [x]
        det6 += [y]
        
    elif abs(y) <= e and x > e:
        tr7  += [x]
        det7 += [y]
        
    elif x <= e and y > x**2/4 + e:
        tr8  += [x]
        det8 += [y]
        
    elif x > e and y > x**2/4 + e:
        tr9  += [x]
        det9 += [y]
        
Saddle        = round(len(det1)/n, 4) 
Sourse        = round(len(det2)/n, 4) 
Sink          = round(len(det3)/n, 4) 
Degen_sourse  = round(len(det4)/n, 6)
Degen_sink    = round(len(det5)/n, 6)
Line_stable   = round(len(det6)/n, 6)
Line_unstable = round(len(det7)/n, 6)
Spiral_sink   = round(len(det8)/n, 4) 
Spiral_sourse = round(len(det9)/n, 4)


# %% Imprimir los datos:

Fig = plt.figure(figsize = (10, 6))
ax  = Fig.add_subplot()

ax.set_title('Clasificacion de estabilidad para matrices 2x2', 
             fontsize = 15)
ax.set_xlabel('Traza de la matriz')
ax.set_ylabel('Determinante de la matriz')

ax.plot(tr1, det1, 'o', label = f'Saddle: {Saddle}', markersize = 2)
ax.plot(tr2, det2, 'o', label = f'Sourse: {Sourse}', markersize = 2)
ax.plot(tr3, det3, 'o', label = f'Sink: {Sink}', markersize = 2)

ax.plot(tr8, det8, 'o', label = f'Spiral Sink: {Spiral_sink}', markersize = 2)
ax.plot(tr9, det9, 'o', label = f'Spiral Sourse: {Spiral_sourse}', markersize = 2)
     
ax.plot(tr4, det4, 'o', label = f'Degenerate Sourse: {Degen_sourse}', markersize = 2)
ax.plot(tr5, det5, 'o', label = f'Degenerate Sink: {Degen_sink}', markersize = 2)
ax.plot(tr6, det6, 'o', label = f'Line Stable: {Line_stable}', markersize = 2)
ax.plot(tr7, det7, 'o', label = f'Line Unstable {Line_unstable}', markersize = 2)

plt.legend()
plt.grid()
plt.show()

plt.savefig("Espectro de matrices.pdf", format = "pdf")