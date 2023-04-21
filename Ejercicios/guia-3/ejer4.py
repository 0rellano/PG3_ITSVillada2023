try:
    num1 = float(input("Ingresar un numero: "))
    num2 = float    (input("Ingresar un numero: "))
    print("El resultado es " + str(num1+num2))
except ZeroDivisionError:
    print("NO PUEDES DIVIDIR POR CERO")
except ValueError:
    print("Ingresa numeros")