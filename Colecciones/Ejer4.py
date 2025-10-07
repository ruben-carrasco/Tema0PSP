lista_ordenada = [int(input("Introduce un número: ")) for _ in range(10)]

list.sort(lista_ordenada,reverse = True)
for num in lista_ordenada:
    print(num)