class Mario():
    def __init__(self):
        print("Examen Mario Lira")

    def primer():
        print("//////////////////////////////")
        print("Identificacion de numero (positivo,negativo, 0)")
        x = float(input("Ingrese un numero: "))
        if x<0:
            print(f"El numero {x} es Negativo")
        elif x>0:
            print(f"El numero {x} es Positivo")
        else:
            print(f"El numero {x} es Neutro")
        print("//////////////////////////////")

    def segundo():
        print("//////////////////////////////")
        while True:
            x = input("Porfavor, escribir la letra de  la elección \n a)Rectangulo \n b)Cuadrado \n c)Tringulo \n d)Salir \n")
            match x:
                case "a":
                    Rectangulo.area()
                case "b":
                    Cuadrado.area()
                case "c":
                    Triangulo.area()
                case "d":
                    break
                case _:
                    print("Favor de escribir una opción correcta")
        print("//////////////////////////////")

    def tercero():
        print("//////////////////////////////")
        Edad = [3,7,88,2,4,55,20,57,42,4,8]
        Bebe = [] 
        Infancia = []
        Adolescenctes = []
        Jovenes = []
        Adultos = []
        for x in Edad:
            #print(x)
            if x<6 and x>=0:
                Bebe.append(x)
            elif x<=11:
                Infancia.append(x)
            elif x<=17:
                Adolescenctes.append(x)
            elif x <=26:
                Jovenes.append(x)
            elif x >=27:
                Adultos.append(x)
            else:
                print("Como hay años negativos????")
        print(f"\n//////////////////////////////\nLista de Bebes: {Bebe}\n//////////////////////////////\nLista de Infancia: {Infancia}\n//////////////////////////////\nLista de Adolescentes: {Adolescenctes}\n//////////////////////////////\nLista de Jóvenes: {Jovenes}\n//////////////////////////////\nLista de Adultos: {Adultos}\n//////////////////////////////\n")
        print("//////////////////////////////")    

        

class Rectangulo():
    def area():
        print("Calcular el area de un rectangulo")
        x = float(input("Favor de escribir la base del rectangulo: "))
        y = float(input("Favor de escribir la altura del rectangulo: "))
        print(f"\n//////////////////////////////\nEl area del rectangulo es de: {x*y}\n//////////////////////////////\n")

class Cuadrado():
    def area():
        print("Calcular el area del cuadrado")
        x = float(input("Favor de escribir un lado del cuadrado: "))
        print("\n//////////////////////////////\nEl area del cuadrado es: ", x**2,"\n//////////////////////////////\n")

class Triangulo():

    def area():
        print("Calcular el area del triangulo")
        x = float(input("Favor de escribir la base del triangulo: "))
        y = float(input("Favor de escribir la altura del triangulo: "))
        print("\n//////////////////////////////\nEl area del triangulo es: ", (x*y)/2,"\n//////////////////////////////\n")

print("Examen POO unidad")
while True:
    v = input("Selecciona el programa a mostrar: \na)Tipo de numero \nb)Calculo de area \nc)Clasificación de edades\nd)Salir \n:")
    match v:
        case "a":
            Mario.primer()
        case "b":
            Mario.segundo()
        case "c":
            Mario.tercero()
        case "d":
            print("Adios :)")
            break
        case _:
            print("Favor de selecionar una respuesta correcta")
