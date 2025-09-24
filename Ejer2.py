# Pedimos al usuario el primer numero y lo guardamos en la variable
num1 = int(input("Introduce el primer número: "))

# Pedimos al usuario el segundo numero y lo guardamos en la variable
num2 = int(input("Introduce el segundo número: "))

# Si el primero numero es mayor, se impre antes el segundo, y si no, lo contrario.
if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)
