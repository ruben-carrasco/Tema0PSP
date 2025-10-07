letras_puntuacion = {}
cont = 0
palabra = ""
puntuacion = 0

#el ord devuelve el unicode de una letra
for letra in range(ord('A'), ord('Z') + 1): #string.ascii_uppercase / map(chr, range(ord('A'), ord('Z') + 1))
    cont += 1
    letras_puntuacion[chr(letra)] = cont

palabra = str(input("Introduce una palabra: "))

# Itero cada letra de la palabra, la busco en el diccionario y sumo su puntuacion
for letra in palabra:
    puntuacion += letras_puntuacion.get(letra.upper(),0)

print(f"Puntuacion de la palabra: {puntuacion}")