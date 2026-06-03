estudiantes = []

nombre_t = input("Ingrese su nombre: ")

print("Hola", nombre_t)

can_est = int(input("Cuántos estudiantes va a registrar: "))

can_notas = int(input("Cantidad de notas de cada estudiante: "))

for i in range(can_est):

    est_nom = input("Ingrese nombre: ")

    notas = []

    for j in range(can_notas):

        nota = float(input("Ingrese la nota: "))

        notas.append(nota)

    promedio = sum(notas) / len(notas)

    estudiante = {
        "Nombre": est_nom,
        "Promedio": promedio
    }

    estudiantes.append(estudiante)

estudiantes.sort(
    key=lambda x: x["Promedio"],
    reverse=True
)


print("\nLISTA FINAL")


for estudiante in estudiantes:

    print(
        estudiante["Nombre"],
        "---",
        estudiante["Promedio"]
    )
