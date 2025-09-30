# Método Main
def main():
    # Pedimos y almacenamos el primero número
    num1 = int(input("Introduce el primer número: "))
    # Pedimos y almacenamos el segundo número
    num2 = int(input("Introduce el segundo número: "))

    # Pasamos por la función las dos variables
    muestraNumeros(num1, num2)

# Función que muestra números entre dos enteros
def muestraNumeros(num1, num2):
    for i in range (num1, num2 + 1):
        print(i, end=" ")

if __name__ == "__main__":
    main()