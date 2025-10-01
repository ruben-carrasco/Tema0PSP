def main():
    contactos = {}
    nombre = ""
    numero = 0

    while(True):
        print("1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Buscar contacto")
        print("0. Mostrar contactos")

        opcion = int(input("Introduce una opcion (1, 2, 3, 0): "))

        match opcion:
            case 1:
                nombre = str(input("Introduce el nombre del nuevo contacto: "))
                numero = int(input("Introduce el número del nuevo contacto: "))
                agregarContacto(nombre,numero,contactos)
            case 2:
                nombre = str(input("Introduce el nombre del contacto: "))
                eliminarContacto(nombre, contactos)
            case 3:
                nombre = str(input("Introduce el nombre del contacto: "))
                buscarContacto(nombre,contactos)
            case 0:
                print(contactos)
            
def agregarContacto(nombre, numero, contactos):
    contactos[nombre] = numero

def eliminarContacto(nombre, contactos):
    del contactos[nombre]

def buscarContacto(nombre,contactos):
    print(contactos.get(nombre,"No encontrado"))

if __name__ == "__main__":
    main()