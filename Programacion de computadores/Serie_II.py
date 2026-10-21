n = int(input('Numero de terminos de la sucesion: '))
n = n - 1
x = 1
y = 1
Sumatoria = x

print(x)

for i in range(0, n, 2):
    x += y
    print(y)
    print(x)
    Sumatoria += x

print ('La sumatoria final es:',Sumatoria)
print('Fin del programa')