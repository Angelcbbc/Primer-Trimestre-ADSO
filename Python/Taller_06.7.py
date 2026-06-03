contraseña=input("Ingrese contraseña: ")
if len(contraseña) >= 8 and any(c.isdigit() for c in contraseña):
    print("Contraseña segura")
else:
    print("Contraseña débil")