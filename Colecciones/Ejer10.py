encriptado = {'e' : 'p','i' : 'v','k' : 'i','m' : 'u','p' : 'm','q' : 't','r' : 'e','s' : 'r','t' : 'k','u' : 'q','v' : 's'}
fraseEncriptada = ""

frase = str(input("Introduce una frase: "))

for letra in frase:
    fraseEncriptada += encriptado.get(letra,letra)

print(fraseEncriptada)