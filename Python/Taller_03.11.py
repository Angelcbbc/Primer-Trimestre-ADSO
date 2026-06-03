nota=float(input("ingrese nota:",))
if nota>5:
    print("numero no valido")
elif nota==5:
    print("!nota maxima!")
elif nota >= 4.5:
    print("excelente")
elif nota >= 4 and nota <= 4.49:
    print("La nota es buena")
elif nota >= 3 and nota <= 3.99:
    print("pasaste")
elif nota >= 2 and nota <= 2.99:
    print("reprobaste")
elif nota >= 0 and nota <= 1.99:
    print("muy mal")   
else:
    print("error")