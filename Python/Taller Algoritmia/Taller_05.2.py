import random
n = int(input("Cantidad de números: "))
numeros = []
for i in range(n):
    numeros.append(random.randint(1, 100))
print(numeros)
suma = sum(numeros)
print("Suma:", suma)