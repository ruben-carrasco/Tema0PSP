# Importamos la clase Random
import random

# Variable con el número random
numRand = random.randint(1, 100)
# Variable booleano que almacena si gana o pierde
ganador = False

# Pedimos un número
num = int(input("Adivina el número: "))

# Bucle que termina si se introduce -1 o gana
while(num != -1 and not ganador): 
    if num > numRand:
        print ("menor")
    elif num < numRand: 
        print("mayor")
    else:
        ganador = True
    # Si no es ganador se vuelve a pedir
    if not ganador: 
        num = int(input("Adivina el número: "))