edad=int(input("Ingrese su edad: ",))
if edad<13:
    print("la edad esta entre 0-12, es un niño")
elif edad<18:
    print("la edad esta entre 13-17, es un joven")
elif edad<60:
    print("la edad esta entre 18-59, es un adulto")
elif edad==60:
    print("la edad es mayor de 59, es un adulto mayor")
elif edad>60:
    print("la edad es mayor de 59, es un adulto mayor")