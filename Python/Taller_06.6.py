carrito=[]
total=0
while True:
    producto=input("producto o salir: ")
    if producto=="salir":
        break
    precio=float(input("precio del producto: "))
    carrito.append(precio)
    total += precio
print("Total de la compra:", total)