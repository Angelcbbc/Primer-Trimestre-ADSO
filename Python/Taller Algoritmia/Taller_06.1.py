notas=[]
for i in range(5):
    nota=float(input("Ingrese la nota del estudiante: "))
    notas.append(nota)
promedio=sum(notas)/len(notas)
if promedio >= 3.0:
    print("El estudiante aprobó.")
else:
    print("El estudiante no aprobó.")   

print("promedio:", promedio)