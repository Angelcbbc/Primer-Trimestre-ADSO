print("Hola")
estudiantes=[]
cantidad_estudiantes=int(input("Cuantos estudiantes desea registrar: ",))
cantidad_notas=int(input("Cuantas notas por estudiante: ",))
for i in range(cantidad_estudiantes):
    nombre=input("nombre del estudiante: ",)
    est_not = []
    for n in range(cantidad_notas):
         nota = float(input("nota del estudiante: "))
         while nota < 0 or nota > 5:
             print("La nota debe estar entre 0 y 5")
             nota = float(input("Nota del estudiante: "))
         est_not.append(nota)
    promedio = sum(est_not) / cantidad_notas
    estudiantes.append((nombre,promedio))
estudiantes.sort(key=lambda x: x[1],reverse=True)
print(estudiantes)
print("El mejor estudiante es: ",estudiantes[0])
buscar = input("Ingrese el nombre a buscar: ").lower()
for estudiante in estudiantes:
    if estudiante[0].lower() == buscar:
        print("Encontrado:", estudiante)
        if estudiante[1]>=3.5:
            print("APROBO")
        else:
            print("REPROBO") 
        break
else:
    print("no existe")