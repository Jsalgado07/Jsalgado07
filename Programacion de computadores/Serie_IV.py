n = int(input('Numero de terminos de la sucesion: '))
x = 1
Sumatoria = 0
for i in range(n):
    x = abs(x) + i 
    x *= (-1) ** ((i+2)%3)
    Sumatoria += x
    print(x)

print ('La sumatoria final es:',Sumatoria)
print('Fin del programa')