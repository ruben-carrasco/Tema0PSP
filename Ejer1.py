# Pedimos el número y casteamos a int el valor de entrada
num = int(input("Ingrese un número: "))

# Si el modulo de 2 es 0, es par, si no impar.
if num % 2 == 0:
    print("El numero " + str(num) + " es par")
else:
    print("El numero " + str(num) + " es impar")