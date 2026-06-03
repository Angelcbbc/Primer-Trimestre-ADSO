usuarios=[]
n=int(input("Ingrese el número de usuarios: "))
for i in range(n):
    nombre=input("Ingrese el nombre del usuario: ")
    edad=int(input("Ingrese la edad del usuario: "))
    usuarios.append((nombre, edad)) 
print(usuarios)


for u in usuarios:
    if u[1] >= 18:
        print(u[0], "es mayor de edad.")