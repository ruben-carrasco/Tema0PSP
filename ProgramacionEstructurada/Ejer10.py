# Método Main
def main():
    # Pedimos y almacenamos el primero número
    num1 = int(input("Introduce el primer número: "))
    # Pedimos y almacenamos el segundo número
    num2 = int(input("Introduce el segundo número: "))

    # Pasamos por la función las dos variables
    print(f"El número más grandes es {obtenerMaximo(num1,num2)}")

# Función que muestra números entre dos enteros
def obtenerMaximo(num1, num2):
    if num1 > num2:
        res = num1
    else:
        res = num2
    return res

if __name__ == "__main__":
    main()