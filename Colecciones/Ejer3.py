lista = [int(input("Introduce un numero: ")) for _ in range(8)]

for num in lista:
    print(f"{num} par" if num % 2 == 0 else f"{num} impar")