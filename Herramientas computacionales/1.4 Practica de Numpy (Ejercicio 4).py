'''
Por:  Daniel Esteba Patiño
      Daniel Santiago Moreno
      Maicol Sanchez
      Valentina Vega Caro
      Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2023-02-25
'''


# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt 
import scipy.stats as stats


# %% Definicion de constantes globales y espacions de memoria:

datos=np.genfromtxt("datos-carro-1d.csv",skip_header=5,delimiter=",",missing_values=np.nan)


# %% Definición de funciones:




# %% Programa principal:




# %% Imprimir los datos:

size = np.arange(len(datos),dtype=float)

t,x,y,ax = size.copy(), size.copy(), size.copy(), size.copy()
for i in range(len(t)): 
    t[i]  = datos[i][0] 
    x[i]  = datos[i][1]
    y[i]  = datos[i][2]

    
plt.plot(t,x),plt.xlabel('tiempo, (s)'),plt.ylabel("posicion en x, (m)"),plt.title("Posicion en x vs t")

#Determinamos que el tiempo inicial es en la línea 35 de los datos
#datos_originales=np.genfromtxt("datos-carro-1d.csv",skip_header=5,delimiter=",",missing_values=np.nan)
datos=np.genfromtxt("datos-carro-1d.csv",skip_header=34,delimiter=",",missing_values=np.nan)
#No_datos=print(len(datos))

size = np.arange(len(datos),dtype=float)
g,j=9.8,0
t,x,y,ax = size.copy(), size.copy(), size.copy(), size.copy()

for i in range(len(t)): 
    t[i]  = datos[i][0] 
    x[i]  = datos[i][1]
    y[i]  = datos[i][2]
    ax[i] = datos[i][5]
    
# print(t)
# print(x)

plt.figure()
plt.plot(t,x)
plt.xlabel('tiempo, (s)')
plt.ylabel("posicion en x, (m)")
plt.title("Posicion en x vs t")


model = np.poly1d(np.polyfit(t, x, 2))

xi = model[2]
vi = model[1]
a  = model[0]*2     # TAREA DE ESTEBAN: Calcular ax promedio de los datos y comparar con este.

ax = ax[2:-2]

prom  = sum(ax)/len(ax)
tt = np.linspace(1, 2.77, 84) 

diff = abs(a - prom)/a*100

plt.figure()
plt.plot(t,x, 'r.', label = 'Datos')
plt.plot(tt, model(tt), 'b', label = 'Función')
plt.xlabel('tiempo, (s)')
plt.ylabel("posicion en x, (m)")
plt.title("Posicion en x vs t")
plt.legend()


