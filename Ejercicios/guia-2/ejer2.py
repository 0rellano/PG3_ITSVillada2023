
class Alumno:
    NOTA_APROBAR = 4

    def set_nombre(self, nombre: str):
        self.nombre = nombre
    
    def set_nota(self, nota: int):
        self.nota = nota
    
    def esta_regular(self):
        if self.nota >= 4:
            print("Estoy regular :D")
        else:
            print("No estoy regular D:")


al1 = Alumno()
al1.set_nombre("pepe")
al1.set_nota(8)
al1.esta_regular()

al2 = Alumno()
al2.set_nombre("Juan")
al2.set_nota(3)
al2.esta_regular()
