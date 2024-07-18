def abstraccion():
    print("La Abstraccion es la capacidad de un lenguaje de programación para representar y manipular conceptos abstractos en el código.")

def encapsulamiento():
    print("La encapsulación es un mecanismo para reunir datos y métodos dentro de una estructura ocultando la implementación del objeto.")

def herencia():
    print("La herencia permite crear clases que reutilizan, extienden y modifican el comportamiento definido en otras clases.")

def polimorfismo():
    print("El polimorfismo es la capacidad que tienen ciertos lenguajes para hacer que, al enviar el mismo mensaje desde distintos objetos, cada uno de esos pueda responder a ese mensaje de forma distinta.")

while True:
    x = input("¿Que definicion quieres conoser?\na)Abstraccion \nb)Encapsulamiento\nc)Herencia\nd)Polimorfismo\ne)salir\n: ")
    match x:
        case "a":
            abstraccion()
        case "b":
            encapsulamiento()
        case "c":
            herencia()
        case "d":
            polimorfismo()
        case "e":
            break
        case _:
            print("Favor de escojer una opcion valida")