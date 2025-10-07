class Articulo:
    def __init__(self, nombre, precio, cuantosQuedan):
        self.nombre = nombre
        self.precio = precio
        self.cuantosQuedan = cuantosQuedan
        self.iva = 21

    def getPVP(self):
        return self.precio * 1.21
    
    def getPVPDescuento(self,descuento):
        return (self.precio * 1.21) * (1 - descuento/100)
    
    def vender(self,cantidad):
        if (self.cuantosQuedan >= cantidad):
            self.cuantosQuedan -= cantidad
            res = True
        else:
            res = False
        return res
    
    def almacenar(self,cantidad):
        self.cuantosQuedan += cantidad

    def __str__(self):
        return f"Artículo: {self.nombre}, Precio (sin IVA): {self.precio}, IVA: {self.iva}%, Stock: {self.cuantosQuedan}"
    
    def __eq__(self, objeto):
        return self.nombre == objeto.nombre

    def __lt__(self, objeto):
        return self.cuantosQuedan < objeto.cuantosQuedan