def sumar():
    while True:
        try:
            num1 = int(input("Ingresar un numero: "))
            num2 = int(input("Ingresar un numero: "))
            print("El resultado es " + str(num1+num2))
        except ValueError:
            print("Los valores ingresados debe ser numeros enteros")
        finally:
            seguir = input("Quiere seguir sumando?('n' para salir)): ")
            if seguir == "n":
                break


if __name__ == "__main__":
    sumar()

