datos=[]
while True:
    print("a. Agregar")
    print("b. Listar")
    print("c. Actualizar")
    print("d. Eliminar")
    print("e. Salir")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        datos.append(input("Ingrese un dato: "))
    elif opcion == 2:
        print("Datos:")
    elif opcion == 3:
        i=int(input("posición: "))
        datos[i] = input("Ingrese el nuevo dato: ")
    elif opcion == 4:
        i=int(input("posición: "))
        datos.pop(i)
    elif opcion == 5:
        break