def promedio(a,b,c):
    return(a+b+c)/3

nombre=input("Ingrese su nombre:",)
print("Bienvenido",nombre,"calculemos tu promedio")

print("Ingresa tus notas")
no1=float(input("Nota-1:",))
no2=float(input("Nota-2:",))
no3=float(input("Nota-3:",))
 
resultado=promedio(no1,no2,no3)
print(nombre,"tu promedio es",resultado)