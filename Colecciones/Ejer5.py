import random

lista = [random.randint(1,11) for _ in range(100)]
cont = 0
n = int(input("Introduce un valor: "))

for i in lista:
    if (i == n):
        cont += 1

print(f"El número {n} aparece {cont} veces")
print(lista)

# lista.count(n)