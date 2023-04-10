class Operacion:

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        print("{} + {} = {}".format(self.a, self.b, self.a + self.b))

    def restar(self):
        print("{} - {} = {}".format(self.a, self.b, self.a - self.b))

    def multiplicar(self):
        print("{} x {} = {}".format(self.a, self.b, self.a * self.b))
    
    def dividir(self):
        if self.b == 0:
            print("no se puede dividr por cero")
            return
        print("{} / {} = {}".format(self.a, self.b, self.a / self.b))

op = Operacion(1, 0)
