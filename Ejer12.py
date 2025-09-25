def main():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    operacion = int(input("Introduce la operación: "))
    resultado = calculadora(num1, num2, operacion)
    print("Resultado:", resultado)

def calculadora(num1, num2, operacion):
    result = 0
    match operacion:
        case 1:
            result = num1 + num2
        case 2:
            result = num1 - num2
        case 3:
            result = num1 * num2
        case 4:
            result = num1 / num2
        case _: 
            result = "Operacion no válida"
    return result


if __name__ == "__main__":
    main()