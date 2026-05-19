nombre="ANGEL"
contraseña=1234
nom=input("Ingresa tu nombre:",)
contra=int(input("Ingrese su contraseña"))
if nombre==nom:
    user=nom
    print("Usuario Correcto")
else:
    print("usuario incorecto")
if contra==contraseña:
    con=contra
    print("Contraseña correcta")
else:
    print("Error de contraseña")
if nombre==nom:
    if contra==contraseña:
        print(user,con,"eres tu?",)
    else:print("error")
else:print("error")


