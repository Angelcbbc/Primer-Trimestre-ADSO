compra=float(input("Valor de compra:",))
if compra==100000:
    descuento=((10*compra)/100)
    print("tu descuento es de:",descuento)
elif compra<100000:
    print("no hay descuento")
else:
    descuento2=((10*compra)/100)
    print("tu descuento es de:",descuento2)