encriptado = {'e' : 'p','i' : 'v','k' : 'i','m' : 'u','p' : 'm','q' : 't','r' : 'e','s' : 'r','t' : 'k','u' : 'q','v' : 's'}
frase_encriptada = ""

frase = str(input("Introduce una frase: "))

for letra in frase:
    frase_encriptada += encriptado.get(letra,letra)

print(frase_encriptada)