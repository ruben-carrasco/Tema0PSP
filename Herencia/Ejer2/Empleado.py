class Empleado:
    def __init__(self, nombre):
        self.__nombre = nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre
    
    def __str__(self):
        return "Empleado " + self.__nombre
    
