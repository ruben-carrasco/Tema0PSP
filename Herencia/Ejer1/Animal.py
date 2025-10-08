class Animal:
    def __init__(self, nombre, num_patas):
        self.nombre = nombre
        self.num_patas = num_patas

    def habla(self):
        return ""

    def __str__(self):
        return f"Me llamo {self.nombre}. tengo {self.num_patas} y sueno asi: {self.habla()}"

        