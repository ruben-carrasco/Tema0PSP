class Libro:
    def __init__(self, titulo, autor, numEjem, numPrestados):
        self.titulo = titulo
        self.autor = autor
        self.numEjem = numEjem
        self.numPrestados = numPrestados

    def prestamo(self):
        if self.numEjem > 0:
            self.numEjem -= 1
            self.numPrestados += 1
            res = True
        else:
            res = False
        return res

    def devolucion(self):
        if self.numPrestados > 0:
            self.numPrestados -= 1
            self.numEjem += 1
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