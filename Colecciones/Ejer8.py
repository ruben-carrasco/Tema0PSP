def main():
    ventas = {}
    nombre = ""
    cantidad_vendida = 0

    while(True):
        print("1. Agregar ventas")
        print("2. Calcular total de ventas")
        print("0. Mostrar ventas")

        opcion = int(input("Introduce una opcion (1, 2, 0): "))

        match opcion:
            case 1:
                nombre = str(input("Introduce el nombre del artículo: "))
                cantidad_vendida = int(input("Introduce el número de artículos vendidos: "))
                agregarVenta(nombre, cantidad_vendida, ventas)
            case 2:
                nombre = str(input("Introduce el nombre del contacto: "))
                print(str(calcularTotalVentas(nombre, ventas)) + " ventas")
            case 0:
                print(ventas)
            
def agregarVenta(nombre, cantidad_vendida, ventas):
    ventas[nombre] = cantidad_vendida

def calcularTotalVentas(nombre, ventas):
    return ventas.get(nombre,0)
    
if __name__ == "__main__":
    main()