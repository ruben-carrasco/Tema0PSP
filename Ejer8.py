# Pedimos el número al usuario
num = int(input("Introduce un número: "))

# Creamos un bucle for para imprimir, va de al numero *
# Se calcula primero el número de espacios y después el de asteriscos
for i in range(0, num):
    print(" " * (num - (i + 1)) + "* " * (i + 1))