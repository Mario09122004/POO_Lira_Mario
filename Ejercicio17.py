class Temperature:
    def celsius_a_fahrenheint():
        x = float(input("Celsius: "))
        print(f"Fahrenheint: {x*(9/5)+32}")

    def fahrenheint_to_celsius():
        x = float(input("Fahrenheint: "))
        print(f"Fahrenheint: {(x-32)*(5/9)}")

while True:
    select = input("¿¿¿Que tipo de convercion desea hacer??? \n a)Celsius a Fahrenheit \n b)Fahrenheit a Celsius \n c)salir\n:")
    match select:
        case "a":
            Temperature.celsius_a_fahrenheint()
        case "b":
            Temperature.fahrenheint_to_celsius()
        case "c":
            print("adios")
            break
        case "A":
            Temperature.celsius_a_fahrenheint()
        case "B":
            Temperature.fahrenheint_to_celsius()
        case "C":
            print("adios")
            break
        case "Celsius a Fahrenheit":
            Temperature.celsius_a_fahrenheint()
        case "Fahrenheit a Celsius":
            Temperature.fahrenheint_to_celsius()
        case "salir":
            print("adios")
            break
        
