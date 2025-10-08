from Animal import Animal

class Gato(Animal):
    def __init__(self, nombre, num_patas):
        super().__init__(nombre,num_patas)

    def habla(self):
        return "Miau"
    
    def __str__(self):
        return "Soy un gato " + super().__str__()
        