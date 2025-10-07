import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def setXY(self,x,y):
        self.x = x
        self.y = y

    def desplaza(self,dx,dy):
        self.x += dx
        self.y += dy

    def distancia(self,punto):
        return math.sqrt((punto.x - self.x) ** 2 + (punto.y - self.y) ** 2)