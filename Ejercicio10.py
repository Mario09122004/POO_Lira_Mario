while True:
    x = int(input("Ingrese un numero: "))
    y = int(input("Ingrese otro numero: "))
    print(f"Su numero sumado es {x+y}")
    salir = input("Desea repetir (n/y): ")
    if salir=="n" or salir=="N" or salir=="no" or salir=="NO":
        break