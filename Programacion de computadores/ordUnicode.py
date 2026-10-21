listaUnicode = []
for i in range(256):
	 a = chr(i)
	 listaUnicode.append(a)

for i in listaUnicode:
	b = ord(i)
	print(f'{i} es {b}')

print ('Fin del programa')
