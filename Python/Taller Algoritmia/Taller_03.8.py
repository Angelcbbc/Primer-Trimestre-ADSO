print("MENU")
print("1.Sumar")
print("2.restar")
print("3.dividir")
print("4.salir")
sele=input("selecione una opcion: ",)
def otravez(sele):
    print("MENU")
    print("1.Sumar")
    print("2.restar")
    print("3.dividir")
    print("4.salir")
    sele01=input("selecione una opcion: ",)
    return sele01
if sele=="1":
    print("SUMAR")
    re=input("quiere volver S/N: ", )
    if re=="S":
        voler=otravez(sele)
        print(voler)
    elif re=="N":
        print("continuemoos")
    else:
        print("ERROR")
elif sele=="2":
    print("restar")
    re=input("quiere volver S/N: ", )
    if re=="S":
        voler=otravez(sele)
        print(voler)
    elif re=="N":
        print("continuemoos")
    else:
        print("ERROR")
elif sele=="3":
    print("dividir")
    re=input("quiere volver S/N: ", )
    if re=="S":
        voler=otravez(sele)
        print(voler)
    elif re=="N":
        print("continuemoos")
    else:
        print("ERROR")
else:
    print("adios")
    re=input("quiere volver S/N: ", )
    if re=="S":
        voler=otravez(sele)
        print(voler)
    elif re=="N":
        print("continuemoos")
    else:
        print("ERROR")