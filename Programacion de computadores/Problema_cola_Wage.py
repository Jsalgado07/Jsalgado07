cola = [list(range(1, 21))]
contador = 20

while True:
    contador += 1
    cola[0] += [contador]
    if (contador-20)%3 == 0:
        for i in range(4):
            cola[0].remove(cola[0][0])
            if len(cola[0]) == 0:
                break
    if len(cola[0]) == 0:
        break

print(f"se atendieron {contador} personas")