def write(text):
    with open("guia-3/archivo.txt", "w") as file:
        try:
            file.write(text)
            file.close
        except TypeError:
            print("Error, no se puede escribir enteros")



texto = "Hola, ¿como estas?"
write(texto)