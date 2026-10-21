a = 400

def fib(n):
	a, b = 0, 1
	c = []
	while a< n:
		c.append(a)
		a, b = b, a+b
	return c

resultado= fib(a)
print(resultado)

print('Fin del programa')