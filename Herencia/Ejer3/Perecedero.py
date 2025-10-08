from Producto import Producto
class Perecedero(Producto):
    def __init__(self, nombre, precio, dias_a_caducar):
        super().__init__(nombre, precio)
        self.dias_a_caducar = dias_a_caducar

    def calculcar(self, cantidad):
        if (self.dias_a_caducar == 1):
            super().calculcar(cantidad) / 4
        elif (self.dias_a_caducar == 2):
            super().calculcar(cantidad) / 3
        elif (self.dias_a_caducar == 3):
            super().calculcar(cantidad) / 2