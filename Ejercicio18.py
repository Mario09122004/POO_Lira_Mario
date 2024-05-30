
productos ={
    "Pan":10,
    "Manzana":5,
    "Chetitos":12,
    "Laptop":7000,
    "Telefono":4000
}
descuento = int(input("De cuanto es el descuento: "))
for x in productos:
    productos[x]=productos[x]-(productos[x]*(descuento/100))

print("///////////////////////////////////////////////")

for x in productos:
    print(f"El precio con descuento de {x} es de {productos[x]}")