def main():
    ventas = {}
    nombre = ""
    cantidadVendida = 0

    while(True):
        print("1. Agregar ventas")
        print("2. Calcular total de ventas")
        print("0. Mostrar ventas")

        opcion = int(input("Introduce una opcion (1, 2, 0): "))

        match opcion:
            case 1:
                nombre = str(input("Introduce el nombre del artículo: "))
                cantidadVendida = int(input("Introduce el número de artículos vendidos: "))
                agregarVenta(nombre, cantidadVendida, ventas)
            case 2:
                nombre = str(input("Introduce el nombre del contacto: "))
                print(str(calcularTotalVentas(nombre, ventas)) + " ventas")
            case 0:
                print(ventas)
            
def agregarVenta(nombre, cantidadVendida, ventas):
    ventas[nombre] = cantidadVendida

def calcularTotalVentas(nombre, ventas):
    return ventas.get(nombre,0)
    
if __name__ == "__main__":
    main()