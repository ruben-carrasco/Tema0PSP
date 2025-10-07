frase = str(input("Introduce una frase: "))
# Separa la frase por espacios y almacena las palabras en una lista
lista_palabras = frase.split()
diccionario = {}

# Hacemos un for-each de la lista
for palabra in lista_palabras:
    # Añadimos un nuevo elemento la clave es la palabra y el valor es 0 si el get no lo encuentra
    # y el valor + 1 si el get lo encuentra
    diccionario[palabra] = diccionario.get(palabra, 0) + 1

print(diccionario)