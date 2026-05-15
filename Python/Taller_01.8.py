print("\nvamos a ver cuanto es tu salario total")
horas=float(input("Cuantas horas trabajas:",))
salario=float(input("Cual es tu salario por horas:",))
disadelmes=int(input("Cuantos dias trabajo:",))
def salarios(horas,salario,diasdelmes):
    horasmes=(diasdelmes*horas*salario)
    return horasmes
respuesta=(salarios(horas,salario,disadelmes))
print("te pagaran:",respuesta,)