print("### 1)Buscar adentro ###")

LISTA = [1, 5, 6, 7]
num = int(input('Ingresar numero: '))

print(LISTA.index(num))



print("### 2)anio bisiesto ###")

def esAnoBisiesto(año: int):
    return año%4 == 0 and año%400 == 0 and año%100 != 0

año = int(input("Ingresar año: "))
if esAnoBisiesto(año):
    print("Es año bisiesto")
else:
    print("No es año bisiesto")



print("### 3)Pintar ###")

def print_cuadrado(caracter, ancho, alto):
    for i in range(alto):
        print(caracter * ancho)

def print_triangulo(caracter, altura):
    count = 1
    espacio = " " * altura

    while count <= altura:
        print(espacio + f"{caracter} " * count )
        count += 1
        espacio = espacio[:-1]


# Bloque Principal

caracter = input('Ingresar caracter para dibujar: ')
print("r - para dibujar rectangulo")
print("t - para dibujar triangulo")
opcion = input()

if opcion == "r":
    ancho = int(input("Ingresar ancho del rectangulo: "))
    alto = int(input("Ingresar alto de rectangulo: "))

    print_cuadrado(caracter, ancho, alto)
elif opcion == "t":
    alto = int(input("Ingresar alto de triangulo: "))
    
    print_triangulo(caracter, alto)
else:
    print("opcion invalida")



print("###  4)orden  ###")

def sort_numeros(lista: list):
    return sorted(lista, reverse=True)


listaNumeros = [5, 2, 1, 4, 3]
print(sort_numeros(listaNumeros))



print("### 5)palindromos ###")

def es_capicuo(palabra):
    palabra = palabra.lower() # paso a minuscula
    return palabra == palabra[::-1]

print(es_capicuo("jovenes"))
print(es_capicuo("neuqueN"))



print("### 6) Contar Vocales ###")

def contar_vocales(frase):
    count = 0
    for letra in frase:
        if letra.lower() in "aeiou":
            count += 1
    return count

print(contar_vocales("Hola como estas"))



print("### 7)numeros step ###")

def es_numero_step(numero: int):
    cadena = str(numero)

    for i in range(len(cadena) - 1):
        numActual = int(cadena[i])
        numSiguiente = int(cadena[i+1])

        if abs(numActual - numSiguiente) != 1:
            return False

    return True

print(es_numero_step(98761787654))
