class Calculadora ():
    def menu ():
        while True:
            x = input(f"\nEscoje la operacion a realizar\na)Suma\nb)Resta\nc)Divicion\nd)Multiplicación\ne)Exponente\nf)Raiz cuadrada\ng)Salir\n:")
            match x:
                case "a":
                    print("/////////////////////////////////////////////////////")
                    print(Calculadora.suma())
                    print("/////////////////////////////////////////////////////")
                case "b":
                    print("/////////////////////////////////////////////////////")
                    print(Calculadora.resta())
                    print("/////////////////////////////////////////////////////")
                case "c":
                    print("/////////////////////////////////////////////////////")
                    print(Calculadora.divicion())
                    print("/////////////////////////////////////////////////////")
                case "d":
                    print("/////////////////////////////////////////////////////")
                    print(Calculadora.multiplicacion())
                    print("/////////////////////////////////////////////////////")
                case "e":
                    print("/////////////////////////////////////////////////////")
                    print(Calculadora.exponente())
                    print("/////////////////////////////////////////////////////")
                case "f":
                    print("/////////////////////////////////////////////////////")
                    print(Calculadora.raiz())
                    print("/////////////////////////////////////////////////////")
                case "g":
                    break
        

    def suma ():
        x = float(input("Numero1 a sumar: "))
        y = float(input("Numero1 a sumar: "))
        return x+y

    def resta ():
        x = float(input("Numero1 a resta: "))
        y = float(input("Numero1 a resta: "))
        return x-y
    
    def multiplicacion ():
        x = float(input("Numero1 a multiplicacion: "))
        y = float(input("Numero1 a multiplicacion: "))
        return x*y
    
    def divicion ():
        x = float(input("Numero1 a divicion: "))
        y = float(input("Numero1 a divicion: "))
        return x/y
    
    def exponente ():
        x = float(input("Numero a base: "))
        y = float(input("Numero del exponente: "))
        return x**y
    
    def raiz ():
        x = float(input("Numero a base: "))
        return x**(1/2)
        

Calculadora.menu()

