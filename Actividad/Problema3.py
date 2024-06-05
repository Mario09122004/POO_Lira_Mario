#Declaramos los conjuntos de números
conjunto1 = {
    123,23456,23456
}
conjunto2 = {
    123,23456,34567
}


#La función pregunta a cuál conjunto se desea agregar un número
def agregar():
    #Los ciclos while lo usamos para que se repita el bloque de código hasta que el usuario registre una opcion valida
    while True:
        try:
            #Se solicita el número para identificar a cuál conjunto se le guardara el número
            y = float(input("Cual conjunto 1/2: "))
            #Si es 1 se guardará en el conjunto 1
            if y == 1:
                #Se solicita el número a guardar
                v = float(input("Numero a ingresar: "))
                #Se agrega el número en el conjunto
                conjunto1.add(v)
                #Se marca que se guardó correctamente
                print("Registro exitoso")
                break
            #Si es 1 se guardará en el conjunto 1
            elif y == 2:
                v = float(input("Numero a ingresar: "))
                conjunto2.add(v)
                print("Registro exitoso")
                break
            else:
                #En caso de error pedimos opcion valida
                print("Favor de poner una opcion valida")
        #Si hay algun error este imprimirá "opcion invalida"
        except:
            print("opcion invalida")
       
def verificar(): #verificar si un número ingresado se encuentra en algún conjunto
    while True:
        try:
            #Se solicita el numero a buscar
            buscar = float(input(f"Ingresa el número a buscar: "))
            #Si se encuentra en el ambos conjuntos este marcara que se encontró en ambos conjuntos
            if buscar in conjunto1 and buscar in conjunto2:
                print(f"El número {buscar} está ene l conjunto uno")
                break
            #Si se encuentra en el conjunto 2 este se marcará que se encontró en el conjunto 2
            elif buscar in conjunto2:
                print(f"El número {buscar} se encuentra en el conjunto dos")
                break
            #Si se encuentra en el conjunto 1 este se marcara que se encontró en el conjunto 1
            elif buscar in conjunto1:
                print(f"El número {buscar} se encuentra en los dos conjuntos")
                break
            else:
                #Si este no se encontro en ningun conjunto marcara que no se encuentra en ningun conjunto
                print(f"El número {buscar} no se encuentra en ningún conjunto")
                break
        except ValueError:
            print(f"Ingresa un número válido")
   
#El ciclo while se repetirá hasta que el usuario desee terminar el programa
while True:
    #Se solicita la opcion a realizar
    x = input("Operacion a realizar \na)Agregar numero \nb)Muestra union \nc)Interseccion \nd)Diferencia \ne)verificar \nf)Salir \n: ")
    #Se revisa que opción fue escogida y se ejecuta su bloque de código correspondiente
    match x:
        case "a":
            agregar()
        case "b":
            union = conjunto1 |conjunto2
            print(f"Union de los conjuntos: {union}")
           
        case "c":


            inter = conjunto1 & conjunto2
            print(f"La interseccion es: {inter}")


        case "d":


            dif = conjunto1-conjunto2
            print(f"La diferen{dif}")
           
        case "e":


            verificar()


        case "f":


            break
           
        case _:
            print("favor de escojer una opcion valida :)")