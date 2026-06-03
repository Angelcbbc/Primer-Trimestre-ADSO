base=float(input("ingrse la base del triangulo:",))
altura=float(input("ingrse la altura del triangulo:",))
def areatriangulo(base,altura):
    area=(base*altura)/2
    return area
area = areatriangulo(base,altura)
print (area)