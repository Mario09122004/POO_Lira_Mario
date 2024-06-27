
#Agregación
class Persona():
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.ine = False
        self.num_trabajos=0
        self.lista_trabajos=[]

    def añadir_trabajo(self,trabajo):
        self.lista_trabajos.append(trabajo)
        self.num_trabajos += 1
        print("Trabajo añadido")

    def mostrar_trabajos(self):
        print(f"tienes {self.num_trabajos} y son:")
        for lista_trabajos in self.lista_trabajos:
            print(lista_trabajos.trabajo)

    def come(self):
        print("*come")

    def tramitar_ine(self):
        self.ine = True
        print("Adquirio su INE")

    def cartera(self):
        if self.ine:
            print(f"Aqui se encuentra su INE")
        else:
            print(f"Aqui no se encuentra su INE")

    def describir(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años")

#Principal
class Trabajo():
    def __init__(self,trabajo):
        self.trabajo = trabajo

    def word(self):
        print("*Hacer un word")

    def exponer(self):
        print("*Expone un tema")

    def descanso(self):
        print("*Toma un descanso")

#Asociación
class Carro():
    def __init__(self,modelo):
        self.modelo = modelo
        self.dueño = []

    def adquisicion_carro(self,persona):
        self.dueño.append(persona)
        print(persona.nombre," tiene el carro ",self.modelo)

    def lista_carros(self):
        print(f"El carro ({self.modelo}) fue adquirido por:")
        for persona in self.dueño:
            print(persona.nombre)

#Composición
class INE():
    def __init__(self,INE):
        self.ine = INE

    def posecion(self):
        if self.ine:
            print("Si tiene INE")
        else:
            print("No tiene INE")

#Herencia
class Alien(Persona):
    def __init__(self, nombre, edad, peso, especie):
        super().__init__(nombre, edad, peso)
        self.especie = especie

    def describir(self):
        super().describir()
        print(f"Mi nombre es {self.nombre}, tengo {self.edad} años y soy de la escie {self.especie}")

    def caminar_por_ahi(self):
        print(f"Estoy paseando")

Mario = Persona("Mario",19,67)
Ricardo = Persona("Ricardo",19,55)

work1 = Trabajo("Programador")
work2 = Trabajo("Diseñador")

carro1 = Carro("Toyota")
carro2 = Carro("Tesla")

alien1= Alien("Juan",19,85,"Marciana")

carro1.adquisicion_carro(Mario)
carro1.adquisicion_carro(Ricardo)
carro2.adquisicion_carro(Ricardo)

carro2.lista_carros()
carro1.lista_carros()

inet = INE(True)
inef = INE(False)

inef.posecion()
inet.posecion()

Ricardo.cartera()
Ricardo.tramitar_ine()
Ricardo.cartera()

alien1.describir()
alien1.caminar_por_ahi()
