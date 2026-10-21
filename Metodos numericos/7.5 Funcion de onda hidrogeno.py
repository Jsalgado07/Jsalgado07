import numpy as np
import matplotlib.pyplot as plt
import Radial
import Angular

from numpy import pi

r = Radial.r
R = Radial.R

g = Angular.g
G = Angular.G

gg = []

for k in range(0, len(g)):
    g_nuevo = g[k] + pi
    gg += [g_nuevo]
    
gg = np.array(gg)

g_entero = np.concatenate((g, gg), axis=0)
G_entero = np.concatenate((G, G), axis=0)

A = []

N = len(r)
M = len(g_entero)
for m in range(0, M):
    F = []
    for n in range(0, N):
        f = (R[n]**2)*(G_entero[m]**2)
        F += [f**0.6]    
    A += [F]


rr, gg = np.meshgrid(r, g_entero)

plt.style.use('dark_background')

Fig, Ax = plt.subplots(subplot_kw=dict(projection='polar'))

Ax.contourf(gg, rr, A, cmap = 'inferno', levels  = 1000)

Ax.text(0.95, 0.15, r'$n = 4$',transform = Ax.transAxes,
        math_fontfamily='cm', fontsize=20, color = 'white')
Ax.text(0.95, 0.05, r'$l = 1$',transform = Ax.transAxes,
        math_fontfamily='cm', fontsize=20, color = 'white')

Ax.set_xticks([])    
Ax.set_yticks([])

plt.show()