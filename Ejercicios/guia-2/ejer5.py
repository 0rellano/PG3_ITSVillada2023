class Persona:

    def crear(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
    
    def imprimir(self):
        print("Hola, soy {} y tengo {}".format(self.nombre, self.edad))


class Empleado(Persona):

    def crear(self, nombre: str, edad: int, sueldo: int):
        super().crear(nombre, edad)
        self.sueldo = sueldo
    
    def imprimir(self):
        super().imprimir()
        print(f"tambien trabajo y cobro {self.sueldo}")

    def tengo_pagar_impuesto(self):
        if self.sueldo > 3000:
            print("Si debes pagar impuestos")
        else:
            print("No debes pagar impuestos")



# Bloque principal

p1 = Persona()

nombre = input("nombre: ")
edad = int(input("edad: "))

p1.crear(nombre, edad)
p1.imprimir()


e1 = Empleado()

nombre = input("nombre: ")
edad = int(input("edad: "))
sueldo = int(input("sueldo: "))

e1.crear(nombre, edad, sueldo)
e1.imprimir()
e1.tengoQuePagarImpuestos()


e2 = Empleado()

nombre = input("nombre: ")
edad = int(input("edad: "))
sueldo = int(input("sueldo: "))

e2.crear(nombre, edad, sueldo)
e2.imprimir()
e2.tengo_pagar_impuesto()