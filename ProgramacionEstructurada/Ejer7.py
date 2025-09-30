# Pedimos y almacenamos el número
num = int(input("Introduce un número positivo: "))
contador = 2
primo = True

# Recorremos del 2 al número, si es divisible por alguno, el booleano
# pasa a true

# Recorremos del 2 al número introducido y paramos cuando sea primo o se llegue al número
while contador < num and primo:
    if num % contador == 0:
        primo = False
    contador += 1

# Imprimimos primo si lo es, o es 1
if primo and num != 1:
    print("primo")
else:
    print("no primo")
