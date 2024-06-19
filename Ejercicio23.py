class Persona():
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def trabaja(self):
        print("*trabaja")

    def come (self):
        print("*trabaja")

    def duerme(self):
        print("*duerme")

Mario = Persona("Mario",19,67)
Ricardo = Persona("Ricardo",19,55)

Mario.trabaja()
Mario.come()
Mario.duerme()
print(f"Edad de {Mario.nombre}: {Mario.edad}")

Ricardo.trabaja()
Ricardo.come()
Ricardo.duerme()
print(f"Edad de {Ricardo.nombre}: {Ricardo.edad}")



#Clases y objetos