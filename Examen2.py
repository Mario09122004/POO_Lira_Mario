import random

#Principal
class Piloto():
    def __init__(self,nombre,edad,fuerza,agilidad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.nivel = 10
        self.compañero = False
        self.habilidad_compañero = None
        self.blade = []
        self.dinero = Economia()
        self.items = Items()
        self.cristales = 0
        self.mision = Misiones ()
        self.enemigos_derrotados = 0

    def explorar(self):
        print(f"Explorando...")
        x = random.choice([True,False,True])
        print(x)
        if x:
            print("aparecio enemigo")
            enemigo = Enemigo()
            enemigo.estadisticas()
            while True:
                v = input(f"Deseas escapar???(Y/N): ")
                if v.upper =="Y":
                    print("*Escapo")
                else:
                    x = random.choice([True,False,False,False])
                    if x:
                        print(f"Pierdes la batalla pero logras escapar")
                        break
                    else:
                        print(f"Atacas al enemigo y lo derrotas (subes nivel y obtienes otras cosas)")
                        self.nivel+=1
                        self.dinero.aumento()
                        self.items.objeto_nuevo()
                        self.fuerza+=2
                        self.agilidad+=2
                        break

    def estadisticas(self):
        print(f"Mi nombre es {self.nombre} tengo {self.edad} años.\nFuerza: {self.fuerza}\nAgilidad: {self.agilidad}\nNivel: {self.nivel}")

    def ataque(self):
        print(f"*ataca")

    def conseguir_compañero(self):
        self.compañero = True
        self.habilidad_compañero = Compañero()
        print(f"Conseguiste compañero {self.habilidad_compañero.hablilidad}")

    def usar_habilidad_compañero(self):
        print(self.compañero)
        if self.compañero:
            print(f"Se uso la habilidad ({self.habilidad_compañero.hablilidad})")
        else:
            print("No se tiene ningun compañero")

    def invocar(self):
        print(f"Se invoco un blade")
        num = Blade(random.randint(0,2))
        self.blade.append(num)

    def revicion_blade(self):
        print(f"Tienes los siguientes blades:")
        for blade in self.blade:
            print(blade.descripcion())
            print(f"////////////////////////////////////////////////////")

    def vienes(self):
        print(self.dinero.checar())

    def opciones_item(self):
        while True:
            print("__________________________________________")
            print("|            Opciones de item            |")
            print("|                                        |")
            print("|Accion a realizar:                      |")
            print("|a)Gastar item                           |")
            print("|b)Conseguir item                        |")
            print("|c)Abrir un cofre                        |")
            print("|d)Exit                                  |")
            print("__________________________________________")
            x = input("¿Cual opcion deseas escojer?")
            match x:
                case "a":
                    self.items.gastar_objeto()
                    break
                case "b":
                    self.items.objeto_nuevo()
                    break
                case "c":
                    Tesoro.abrir(self.items)
                    break
                case "d":
                    break
                case _:
                    print("Escoge una opcion correcta")
        #Insertar opciones para recolectar o usar item
    
    def hacer_mision(self):
        self.mision.mostrar_estado()
        
#Dependencia
class Misiones():
    def __init__(self):
        self.tipo = random.choice(["Principal", "Secundaria"])
        self.estado = True

    def mostrar_estado(self):
        if self.estado:
            print(f"La mision es {self.tipo} y esta activa")
        else:    
            print(f"La mision es {self.tipo} y esta desactivada")

    def desactivar(self):
        self.estado = False
        print(f"Se desactivo la mision")

    def activar(self):
        self.estado = True
        print(f"Se activo la mision")


#Asociación
class Tesoro():
    def __init__(self):
        pass

    def abrir(item):
        x = random.choice([True,False])
        if x:
            item.objeto_nuevo()
        else:
            item.gastar_objeto()

#Asociacion
class Items():
    def __init__(self):
        self.otros = 10

    def objeto_nuevo(self):
        self.otros += 1
        print(f"Se agrego un objeto \nCantidad de objetos: {self.otros}")

    def gastar_objeto(self):
        self.otros -= 1
        print(f"Se elimino un objeto \nCantidad de objetos: {self.otros} (o lo usaste o te lo robo un mimic)")

#Asociación
class Economia():
    def __init__(self):
        self.dinero = 10

    def aumento(self):
        self.dinero += 1
        print(f"Dinero actual: {self.dinero}")

    def reduccion(self):
        self.dinero -= 1
        print(f"Dinero actual: {self.dinero}")
    
    def checar(self):
        print(f"Dinero actual: {self.dinero}")

#Herencia
class Enemigo(Piloto):
    def __init__(self):
        self.nivel = random.randint(1,50)
        matriz = [
            ["Esqueleto", 2*self.nivel, 1*self.nivel],
            ["Zombie", 2*self.nivel, 1*self.nivel],
            ["Diablo", 2*self.nivel, 1*self.nivel]
        ]
        num = random.randint(0,2)
        self.nombre = matriz[num][0]
        self.edad = 0
        self.fuerza = matriz[num][1]
        self.agilidad = matriz[num][2]


    def estadisticas(self):
        super().estadisticas()


#Agregación
class Blade():
    def __init__(self,num):
        matriz = [
            ["Geo", 10, 30],
            ["V", 30, 10],
            ["Itadory", 20, 20]
        ]
        self.nombre = matriz[num][0]
        self.ataque = matriz[num][1]
        self.defensa = matriz[num][2]

    def descripcion(self):
        print(f"Mi nombre es {self.nombre}\nMi ataque es de {self.ataque}\nMi defensa es de {self.defensa}")
        

#Compocición
class Compañero():
    def __init__(self):
        nombre=["Juan","Pedro","Mario","Yuta","Maki"]
        self.nombre = nombre[random.randint(0,4)]
        self.edad = 20
        self.hablilidad = "Mejora la fuerza y agilidad del personaje"

    def descripcion(self):
        print(f"Soy {self.nombre} tengo {self.edad} años y mi abilidad es {self.hablilidad}")

##########################################################################################
print(f"Simulacion de un juego :)")
a = input(f"Nombre del personaje:")
b = input(f"Edad del personaje:")
personaje = Piloto(a,b,random.randint(5, 10),random.randint(5, 10))

while True:
    #Menú
    print("_________________________________________")
    print("|          Simulacion de juego          |")
    print("|                                       |")
    print("|Accion a realizar:                     |")
    print("|a)Explorar                             |")
    print("|b)Ver estadisticas                     |")
    print("|c)Ataque                               |")
    print("|d)Conseguir compañero                  |")
    print("|e)Usar habilidad de compañero          |")
    print("|f)Invocar blade                        |")
    print("|g)Revisar blades                       |")
    print("|h)Dinero                               |")
    print("|i)Opciones de Item                     |")
    print("|j)Mision                               |")
    print("|k)Salir                                |")
    print("|                                       |")
    print("_________________________________________")
    x = input("¿Cual opcion deseas escojer?")
    match x:
        case "a":
            personaje.explorar()
        case "b":
            personaje.estadisticas()
        case "c":
            personaje.ataque()
        case "d":
            personaje.conseguir_compañero()
        case "e":
            personaje.usar_habilidad_compañero()
        case "f":
            personaje.invocar()
        case "g":
            personaje.revicion_blade()
        case "h":
            personaje.vienes()
        case "i":
            personaje.opciones_item()
        case "j":
            personaje.hacer_mision()
        case "k":
            break
        case _:
            print("Escoge una opcion correcta")
