def fib(n+1):
	
	if n < 2:
		return n
	return fib(n - 1) + fib(n - 2)

for i in range(15):
	print(fib(i))