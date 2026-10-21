'''
Por: Juan Diego Salgado Giraldo
Correo: jsalgadog@unal.edu.co
Fecha: 2022-MM-DD
'''
'''
Write a function that receives a positive integer and returns a list
with all its prime factors
'''
'''
Juan Diego Salgado Giraldo
Jose Miguel Chavez
Daniel Felipe Castellanos Rivera
Santiago Nova Acosta
Fabián Ricardo Hernández Gáfaro
Leidy Guevara
'''


# %% Importación de librerías:

import numpy as np


# %% Definición de funciones:

def primefactors(n):
    D = [i for i in range(2, n+1) if n%i == 0] # Selecciona los divisores
    P = []                                     # Espacio de memoria para los primos     
    for m in D:                                # Selecciona los primos de los divisores
        if isprime(m) == True:
            P += [m]
        else:
            continue
    return P
    

def isprime(n):                                     
    D = [i for i in range(2, n+1) if n%i == 0]  # Selecciona los divisores
    if len(D) == 1:                             # Si es primo
        return True
    else:
        return False


# %% Imprimir los datos:

print(primefactors(2))
print(primefactors(10))
print(primefactors(201))
print(primefactors(97))
print(primefactors(1213427))
print(primefactors(1213428))


