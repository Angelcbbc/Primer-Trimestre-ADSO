import random
numeros=random.randint(1,10)
for i in range(5):
    intento=int(input("Adivina el número entre 1 y 10: "))
    if intento==numeros:
        print("¡Felicidades! Adivinaste el número.")
    elif intento<numeros:
        print("El número es mayor.")
    else:
        print("El número es menor.")
print("El número era:", numeros)