class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calculcar(self, cantidad):
        return self.precio * cantidad

    def __str__(self):
        return f"Nombre: {self.nombre}. Precio: {self.precio}"
    
    def __lt__(self, otro_objeto):
        return self.precio < otro_objeto.precio
        