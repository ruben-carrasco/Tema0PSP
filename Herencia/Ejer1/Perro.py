from Animal import Animal

class Perro(Animal):
    def __init__(self, nombre, num_patas):
        super().__init__(nombre,num_patas)

    def habla(self):
        return "Guau"
    
    def __str__(self):
        return "Soy un perro " + super().__str__()
    
