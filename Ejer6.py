# Variable que almacena el numero introducido por el usuario
num = int(input("Introduzca un número: "))
# Contador para el multiplicador
contador = num
# Variable para el factorial
factorial = num

# Se decrementa el multiplicador y se multiplica por factorial hasta que llega a 1
while contador > 1:
    contador -= 1
    factorial *= contador

# Imprimimos el resultado
print(f"{num}! = {factorial}")