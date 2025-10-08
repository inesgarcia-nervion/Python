''' 1. Define una clase llamada Animal que tiene como atributos nombre y número de patas.
Además del constructor, define los siguientes métodos:


    a.habla: En la clase Animal devolverá una cadena vacía, ‘’.
    b.__str__: Devolverá una cadena de la siguiente forma: “Me llamo nombre, tengo x patas y sueno así: sonido”.
    Habrá que sustituir lo que está en azul por el nombre y el número de patas del animal. En el caso de sonido
    hay que llamar a la función habla.


A continuación, define dos clases, Gato y Perro que heredan de Animal. En el caso de Gato, además del constructor,
definirá los siguientes métodos:
    a.habla: Devolverá ‘Miau’.
    b.__str__: Primero escribirá “Soy un gato” y a continuación la misma cadena que el padre.


En el caso de Perro, además del constructor, definirá los siguientes métodos:
    a.habla: Devolverá “Guau”.
    b.__str__: Primero escribirá “Soy un perro” y a continuación la misma cadena que el padre.'''


class Animal:
    def __init__(self, nombre, numPatas):
        self.nombre = nombre
        self.numPatas = numPatas
    

    def habla(self):
        return ''
    

    def __str__(self):
        return f"Me llamo {self.nombre}, tengo {self.numPatas} patas y sueno así: {self.habla()}"
    

class Gato(Animal):
    def __init__(self, nombre, numPatas):
        super().__init__(nombre, numPatas)

    def habla(self):
        return "Miau"

    def __str__(self):
        return f"Soy un gato. {super().__str__()}"



class Perro(Animal):
    def __init_(self, nombre, numPatas):
        super().__init__(nombre, numPatas)

    def habla(self):
        return "Guau"

    def __str__(self):
        return f"Soy un perro. {super().__str__()}"



#Pruebas
animal1 = Animal("Kira", 4)
animal2 = Gato("Bigotitos", 4)
animal3 = Perro("Rocky", 4)


print(animal1)
print(animal2)
print(animal3)



print(animal1.habla())
print(animal2.habla())
print(animal3.habla())