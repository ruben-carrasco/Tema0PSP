listaOrdenada = [int(input("Introduce un número: ")) for _ in range(10)]

list.sort(listaOrdenada,reverse = True)
for num in listaOrdenada:
    print(num)