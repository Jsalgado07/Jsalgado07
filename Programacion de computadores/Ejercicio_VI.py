Valor_inicial = 0
Valor_final = int(input('Valor Final='))

lista_impares = []
def numeros_impares(a,b):
    c = list(range(a,b))
    for i in c:
    	if i%2 != 0:
            lista_impares.append(i)
    return(lista_impares)

fun = numeros_impares(Valor_inicial, Valor_final)

print(fun)
print()
print('Fin del programa')
