x = float(input("Ingresar el peso del paquete a enviar (Kg): "))
if x <1:
    print("$50")
elif x<5:
    print("$100")
elif x<10:
    print("$200")
else:
    print("$500")