ingre=int(input("caculemos tus impuestos, dime tus ingresos:",))
if ingre<1500000:
    print("libre de impuestos")
elif ingre==1500000:
    print("libre de impuestos")
elif ingre<3000000:
    print("impuestos del 10%",)
    impues1=((10*ingre)/100)
    print("impuesto de:",impues1)
elif ingre==3000000:
    print("impuestos del 10%",)
    impues1=((10*ingre)/100)
    print("impuesto de:",impues1)
elif ingre>3000000:
    print("impuesto del 20%:",)
    impues2=((10*ingre)/100)
    print("impuesto de",impues2)
else:
    print("error")