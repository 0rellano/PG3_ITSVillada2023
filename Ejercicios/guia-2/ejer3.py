
class Triangulo:

    def crear(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
    
    def mostar_lado_mayor(self):
        mayor = 0
        for num in [self.lado_a, self.lado_b, self.lado_c]:
            if num > mayor: mayor = num
        print(mayor)

    def es_equilatero(self):
        if self.lado_a == self.lado_b == self.lado_c:
            print(f"Es un triangulo equilatero")
        else:
            print("Esn't un triangulo equilatero")

t1 = Triangulo()
t1.crear(1, 2, 3)
t1.mostar_lado_mayor()
t1.es_equilatero()

t2 = Triangulo()
t2.crear(1, 1, 1)
t2.mostar_lado_mayor()
t2.es_equilatero()