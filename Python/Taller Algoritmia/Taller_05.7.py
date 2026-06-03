numeros = [10, 20, 30, 40]
buscar = int(input("Número a buscar: "))
if buscar in numeros:
    posicion = numeros.index(buscar)
    print("Posición:", posicion)
else:
    print("No existe")