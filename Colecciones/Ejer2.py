lista = [int(input("Ingrese un número: ")) for _ in range(10)]
max = 0
min = 0

# Ordeno la lista de menor a mayor
lista.sort()

max = lista[-1]
min = lista[0]

#min(lista)
#max(lista)

print("Max: " + str(max))
print("Min: " + str(min))

