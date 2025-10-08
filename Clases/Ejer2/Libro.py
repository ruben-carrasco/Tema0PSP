class Libro:
    def __init__(self, titulo, autor, num_ejem, num_prestados):
        self.titulo = titulo
        self.autor = autor
        self.num_ejem = num_ejem
        self.num_prestados = num_prestados

    def prestamo(self):
        if self.num_ejem > 0:
            self.num_ejem -= 1
            self.num_prestados += 1
            res = True
        else:
            res = False
        return res

    def devolucion(self):
        if self.num_prestados > 0:
            self.num_prestados -= 1
            self.num_ejem += 1
            res = True
        else:
            res = False
        return res

    def __str__(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nEjemplares: {self.numEjem}\nPrestados: {self.numPrestados}"
        
    def __eq__(self, objeto):
        return self.titulo == objeto.titulo and self.autor == self.autor
        
    def __lt__(self, objeto):
        return self.autor < objeto.autor