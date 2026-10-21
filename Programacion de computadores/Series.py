n = int(input('Numero de terminos de la sucesion: '))
x = 1
Sumatoria = 0
for i in range(n):
    x += i
    print(x)
    Sumatoria += x

print ('La sumatoria final es:',Sumatoria)
print('Fin del programa')