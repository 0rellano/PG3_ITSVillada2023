class Familias:

    def __init__(self, padre: str, madre: str, *hijos):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos

    def __str__(self):
        return "Padre: {}; Madre: {}; Hijos: {}".format(self.padre, self.madre,", ".join(self.hijos))



familia = Familias("Jorque", "juana", "raul, jorgito, raul")
print(familia)