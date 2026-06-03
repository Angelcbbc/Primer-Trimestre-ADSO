cantidad = int(input("¿Cuántos números va a ingresar?: "))
positivos = 0
for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    if numero > 0:
        positivos = positivos + 1
print("Cantidad de números positivos:", positivos)