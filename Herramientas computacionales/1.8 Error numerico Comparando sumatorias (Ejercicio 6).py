'''
Por: Nelson Andres Rodriguez Mora
     Juan Diego Salgado Giraldo 
     David Alexander Rubio Pedraza
     Jorge Luis Jaramillo Gaitan
     David Alejandro Marin Rincon
Correo: jsalgadog@unal.edu.co
Fecha: 2023-03-03
'''

# %% Importación de librerías:

import numpy as np
import matplotlib.pyplot as plt
from numpy import ones, cumsum


# %% Definición de funciones:

def sum1(N):
    n  = np.arange(1,2*N+1)
    y1 = cumsum(np.power(-ones(2*N),n)*n/(n + ones(2*N)))
    return y1[-1]

def sum2(N):
    n  = np.arange(1,N+1)
    y2 = -cumsum((2*n - ones(N))/(2*n)) + cumsum(2*n/(2*n + ones(N)))
    return y2[-1]

def sum3(N):
    n  = np.arange(1,N+1)
    y3 = cumsum(ones(N)/(2*n*(2*n + ones(N))))
    return y3[-1]


def plot_diff_sums(N):
    """
    Plots the relative difference among three sums which are the same mathematically
    """
    adata = np.zeros(N+1)
    bdata = np.zeros(N+1)
    for n in range(1, N+1):
        adata[n] = abs((sum1(n) - sum3(n))/sum3(n))
        bdata[n] = abs((sum2(n) - sum3(n))/sum3(n))

    fig, axes = plt.subplots()
    axes.plot(adata, "o-", ms=6.0, label="%sum1")
    axes.plot(bdata, "g*--", ms = 9.0, label="%sum2")
    axes.set_xscale("log")
    axes.set_yscale("log")
    axes.legend(loc=2)


# %% Imprimir los datos

plot_diff_sums(1000)


