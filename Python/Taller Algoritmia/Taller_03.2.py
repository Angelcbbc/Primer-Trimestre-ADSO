lado1=float(input("diga el valor de uno de los lados del triangulo: ",))
lado2=float(input("diga el valor de uno de los lados del triangulo: ",))
lado3=float(input("diga el valor de uno de los lados del triangulo: ",))
if lado1==lado2 and lado2==lado3:
    print("el triangulo es equilatero")
elif lado1==lado2 or lado2==lado3 or lado1==lado3:
    print("el triangulo es isoceles")
else:
    print("el triangulo es escaleno")