Lista = ['Carlos', 'Isabel', 'Adriana', 'Gabriel', 'María', 'Ernesto', 'Yadira', 'Carlos']

for i in range(len(Lista)):
   print(i, Lista[i])

print('La longitud de la lista es de: ' + str(len(Lista)))

Conteo = Lista.count('Carlos')
print('El Nombre de "Carlos" esta ',Conteo,'veces')

print()
print('Fin del programa')