#Pasar parametros a una funcion

def fun(a, b):
    a.append('xyz')
    b = b + 10 

L = [1, 2,3 ]
X = 10

print(L)
print(X)

fun(L, X)
print(L)
print(X)

fun(L[:], X)
print(L)
print(X)

print('Fin del programa')
