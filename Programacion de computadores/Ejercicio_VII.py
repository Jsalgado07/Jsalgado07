b = int(input('Valor Final='))

lista_No_primos = []
Lista_total = list(range(1,b+1))
Lista_primos = []

for i in range (2,b+1):
	for x in range(2,i):
		if i%x ==0: 
			lista_No_primos.append(i)
			break
	else:
		Lista_primos.append(i)

print('lista de Numeros evaluados: ', Lista_total)
#print(lista_No_primos)
print('Lista de numeros primos pertenecientes a la evaluacion: ',Lista_primos)
print()
print('Fin del programa')

#for n in range(2,15):
	#for x in range (2, n):
		#if n%x ==0:
			#print(n, "igual a ", x, "*", n//x)
			#break