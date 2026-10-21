'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-02-25
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt 

from scipy import optimize as op


# %% Definicion de constantes globales y espacions de memoria:

datos=np.genfromtxt("datos-carro-1d.csv",skip_header=34,delimiter=",",
                    missing_values=np.nan)

t = datos[:, 0]
x = datos[:, 1]
v = datos[:, 3]
a = datos[:, 5]

a = a[:-2]

n = len(x)


# %% Definición de funciones:

def Def_central(x, t):
    
    DX = []
    
    for i in range(n):
        if i == 0 or i == n-1:
            continue
        else:
            h  = t[i] - t[i-1]
            dx = (x[i+1]-x[i-1])/(2*h)
            DX += [dx]
    
    return DX

def linear(t, a, b):
    return a*t + b

def cuadratic(t, a, b, c):
    return a*t**2 + b*t + c


# %% Programa principal:

v_num = Def_central(x, t)

par_v, cov_v = op.curve_fit(linear, t[1:-1], v_num)

a_num  = round(par_v[0], 4)
vi_num = round(par_v[1], 4)

desv_a  = round(cov_v[0, 0], 5)
desv_vi = round(cov_v[1, 1], 5)


par_a, cov_a = op.curve_fit(cuadratic, t, x)

a_num2 = round(par_a[0]*2, 4)
prom_a  = round(sum(a)/len(a), 4)

diff1 = round(abs(prom_a - a_num)/prom_a, 4)
diff2 = round(abs(prom_a - a_num2)/prom_a, 4)

# %% Imprimir los datos:

fig = plt.figure(figsize = (10, 6)) 
ax  = fig.add_subplot()

ax.plot(t, v,'ro', label = 'Datos experimentales')
ax.plot(t[1:-1], v_num, 'b*', label= 'Datos numericos')
ax.plot(t, linear(t, *par_v), 'black', 
        label = f'Curva de ajuste $v(t)=v_o+at$ \n $v_o={vi_num}\pm {desv_vi}$ \n $a={a_num} \pm {desv_a}$')

ax.set_xlabel('tiempo (s)')
ax.set_ylabel("velocidad en x, (m/s)")
ax.set_title("Velocidad en x vs t")

plt.legend()
plt.show()


fig = plt.figure(figsize = (10, 6)) 
ax  = fig.add_subplot()

ax.plot(t[:-2], a,'o', label = f'Datos experimentales con promedio $a = {prom_a}$')
ax.plot(t, [a_num]*n, label= f'Curva con datos de la velocidad \n $a={a_num}$ \n $Error={diff1}$')
ax.plot(t, [a_num2]*n, label = f'Curva con datos de la posicion \n $a={a_num2}$ \n $Error = {diff2}$')

ax.set_xlabel('tiempo (s)')
ax.set_ylabel("aceleracion en x, (m/s^2)")
ax.set_title("Aceleracion en x vs Tiempo")

plt.legend()
plt.show()




