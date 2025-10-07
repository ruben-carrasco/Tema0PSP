class CuentaCorriente:
    def __init__(self, dni, saldo, nombre = ""):
        self.dni = dni
        self.saldo = saldo
        self.nombre = nombre
    
    def __init__(self, dni, nombre, saldo):
        self.dni = dni
        self.nombre = nombre
        self.saldo = saldo
    
    def sacarDinero(self, cantidad):
        if (self.saldo > cantidad):
            self.saldo -= cantidad
            res = True
        else:
            res = False
        return res
    
    def ingresarDinero(self, cantidad):
        self.saldo += cantidad

    def __str__(self):
        return f"DNI: {self.dni}\nNombre: {self.nombre}\nSaldo: {self.saldo}"
    
    def __eq__(self, objeto):
        return self.dni == objeto.dni
    
    def __lt__(self, objeto):
        return self.saldo < objeto.saldo
        

    