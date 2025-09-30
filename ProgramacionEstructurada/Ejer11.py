# Método Main
def main():
    # Pedimos y almacenamos un caracter
    char = input("Introduce un carácter: ")

    # Si la funcion devuelve true es vocal, si no no.
    if averiguarVocal(char):
        print("Es vocal")
    else:
        print("No es vocal")

# Función que muestra números entre dos enteros
def averiguarVocal(char):
    esVocal = False
    # Comprueba que es una letra
    if char.isalpha():
        char = char.upper() # Lo pasa a mayusculas
        if char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
            esVocal= True
    return esVocal

if __name__ == "__main__":
    main()