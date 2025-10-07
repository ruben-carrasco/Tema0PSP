class Articulo:
    def __init__(self, nombre, precio, cuantos_quedan):
        self.nombre = nombre
        self.precio = precio
        self.cuantos_quedan = cuantos_quedan
        self.iva = 21

    def getPVP(self):
        return self.precio * 1.21
    
    def getPVPDescuento(self,descuento):
        return (self.precio * 1.21) * (1 - descuento/100)
    
    def vender(self,cantidad):
        if (self.cuantos_quedan >= cantidad):
            self.cuantos_quedan -= cantidad
            res = True
        else:
            res = False
        return res
    
    def almacenar(self,cantidad):
        self.cuantos_quedan += cantidad

    def __str__(self):
        return f"Artículo: {self.nombre}, Precio (sin IVA): {self.precio}, IVA: {self.iva}%, Stock: {self.cuantos_quedan}"
    
    def __eq__(self, objeto):
        return self.nombre == objeto.nombre

    def __lt__(self, objeto):
        return self.cuantos_quedan < objeto.cuantos_quedan