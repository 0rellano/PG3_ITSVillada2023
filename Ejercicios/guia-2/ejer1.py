
class Persona:

    def definir_nombre(self, nombre):
        self.nombre = nombre
    
    def presentarse(self):
        print(f"Hola, soy {self.nombre}")



p1 = Persona()
p2 = Persona()

p1.definir_nombre("Pepe")
p2.definir_nombre("Juancito")

p1.presentarse()
p2.presentarse()

