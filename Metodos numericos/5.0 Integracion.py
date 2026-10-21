"""

Evaluacion de intregrales definidas a travez de los siguientes metodos:
    
    - Regla del rectangulo
    - Regla del trapecio
    - Regla de Simpson 1/3 
    - Regla de simpson 1/3 multiple

"""

'''
Comandos basicos
'''

import sympy as sp

x = sp.symbols('x') 
y = sp.symbols('y')
f = sp.sin(x)

I_ind = sp.integrate(f, x)
I_def = sp.integrate(f, (x, 0, 1.5))
