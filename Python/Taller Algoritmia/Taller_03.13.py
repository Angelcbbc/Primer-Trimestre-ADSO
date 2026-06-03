usuario = input("Ingrese usuario: ").lower()

contraseña = input("Ingrese contraseña: ")

rol = input("Ingrese rol: ").lower()


if usuario == "admin" and contraseña == "1234" and rol == "admin":

    print("Acceso permitido")

else:

    print("Acceso denegado")