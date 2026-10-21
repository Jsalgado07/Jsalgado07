n = int(input("Escriba hasta donde quiere que vaya la serie:  "))
res = 0
for i in range(1, n+1):
		res += (((-1)**(i+1))/i)
print(res)
print()
print("FIN HPTA")