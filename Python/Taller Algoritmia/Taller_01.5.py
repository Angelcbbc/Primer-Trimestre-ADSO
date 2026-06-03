radio=float(input("Ingrese radio del circulo:"))
pie=3.1416
def circuloradio(radio,pie):
    area=(pie*radio**2)    
    return area
area= circuloradio(radio,pie)
print ("El area del circulo es:",area)