class Persona():
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
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


class Trabajo():
    def __init__(self,trabajo):
        self.trabajo = trabajo

    def word(self):
        print("*Hacer un word")

    def exponer(self):
        print("*Expone un tema")

    def descanso(self):
        print("*Toma un descanso")


Mario = Persona("Mario",19,67)
Ricardo = Persona("Ricardo",19,55)

work1 = Trabajo("Programador")
work2 = Trabajo("Diseñador")

Mario.añadir_trabajo(work1)
Mario.mostrar_trabajos()
Mario.come()

Ricardo.añadir_trabajo(work1)
Ricardo.añadir_trabajo(work2)
Ricardo.mostrar_trabajos()
Ricardo.come()

#Programa 24 - Clases y objetos complementario