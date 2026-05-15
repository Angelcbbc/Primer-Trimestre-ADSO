valor1=input("NGRESE PRIMER DATO:",)
valor2=input("INGRESE SEGUNDO DATO:",)
print ("Antes:",
       "Primero:",valor1,
       "Segundo:",valor2)
def cruse(valor1,valor2):
    valor1, valor2=valor2,valor1
    return valor1 , valor2
nuevo1,nuevo2= cruse(valor1,valor2)
print("DESPUES",
      "Primero:",nuevo1,
      "Segundo:",nuevo2)