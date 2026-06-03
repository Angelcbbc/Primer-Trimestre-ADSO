import random
numero_secreto = random.randint(1, 10)
intento = 0
while intento != numero_secreto:
    intento = int(input("Adivine el número (1-10): "))
    if intento < numero_secreto:

        print("El número es mayor")
    elif intento > numero_secreto:

        print("El número es menor")
    else:
        print("¡Correcto!")