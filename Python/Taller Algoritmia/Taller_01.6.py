celsius=float(input("ingrese temperatura en celsius:",))
def convertirtem(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
print ("El resultado es ",convertirtem(celsius),"grados FAHRENHEIT")