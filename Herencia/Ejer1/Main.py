from Animal import Animal
from Perro import Perro
from Gato import Gato

animal = Animal("Firu",1)

gato = Gato("Michi",4)

perro = Perro("Pepe",4)

print(animal, animal.habla())
print(gato, gato.habla())
print(perro, perro.habla())