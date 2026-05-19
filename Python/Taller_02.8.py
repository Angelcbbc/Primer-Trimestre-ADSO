nota=float(input("ingrese nota:",))
if nota>5:
    print("numero no valido")
elif nota==5:
    print("!nota maxima!")
elif nota>3.5:
    print("pasaste")
elif nota<3.5:
    print("repobaste")
elif nota==3.5:
    print("apenas pasaste")
else:
    print("error")