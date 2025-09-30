# Variable que almacena la suma de los numeros
suma = 0

# Pedimos un numero positivo al usuario
num = int(input("Introduzca un número positivo: "))

# Bucle que termina cuando el numero sea negativo
while(num >= 0):
    # Sumamos el numero a la suma total
    suma += num
    # Pedimos un nuevo número
    num = int(input("Introduzca un número positivo: "))

# Mostramos la suma
print(f"Suma: {suma}")
