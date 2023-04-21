MESES = ("enero",
          "febrero",
          "marzo",
          "abril",
          "mayo",
          "junio",
          "agosto",
          "septiembre",
          "agosto",
          "octubre",
          "noviembre",
          "diciembre")
try:
    numMes = input("Ingresar numero de un mes")
    print("Mes elegido: " + MESES[numMes])
except IndexError:
    print("El numero que elegiste no pertenece a ningun mes")
except ValueError:
    print("Tienes que ingresar un NUMERO")

