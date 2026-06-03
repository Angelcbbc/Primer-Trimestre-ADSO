numero1 =int(input("Ingrese el primer numero:",))
numero2 =int(input("ingrese el segundo numero:",))
def operaciones(numero1,numero2):
    multiplicar=(numero1 * numero2)
    sumar= (numero1 + numero2)
    restar=(numero1-numero2)
    if numero2==0:
        print ("No es posible dividir entre 0")
        dividir="error"
    else:
         dividir=(numero1/numero2)
    return sumar,restar,multiplicar,dividir
resultados=(operaciones(numero1,numero2))
print (resultados)
print ("Eso es todo")
