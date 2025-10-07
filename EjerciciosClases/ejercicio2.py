'''2. Crea una clase llamada Libro que guarde la información de cada uno de los libros de una biblioteca.
La clase debe guardar el título del libro, autor, número de ejemplares del libro y número de ejemplares prestados.
La clase contendrá los siguientes métodos:


    a.Constructor con todos los parámetros (se le indica valores para todos los atributos).
    b.prestamo(): incrementa el atributo correspondiente cada vez que se realice un préstamo.
    No se pueden prestar libros si no quedan ejemplares disponibles para prestar. Devuelve true si se ha
    podido realizar el préstamo y false en caso contrario.
    c.devolucion(): decrementa el atributo correspondiente cada vez que se devuelva un libro. No se podrán
    devolver libros que no se hayan prestado. Devuelve true si se ha podido realizar la operación y false en
    caso contrario.
    d.Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos  libros son iguales si tienen
    el mismo título y el mismo autor. Los libros se ordenarán de menor a mayor por el nombre del autor. '''

class Libro:
    def __init__(self, titulo, autor, numEjemplares, numPrestados):     #Constructor con todos los parámetros
        self.titulo = titulo
        self.autor = autor
        self.numEjemplares = numEjemplares
        self.numPrestados = numPrestados


    def prestamo(self):
        if self.numEjemplares > self.numPrestados:
            self.numPrestados += 1
            return True
        else:
            return False
        

    def devolucion(self):
        if self.numPrestados > 0:
            self.numPrestados -= 1
            return True
        else:
            return False


    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Número de ejemplares: {self.numEjemplares}, Número de ejemplares prestados: {self.numPrestados}"


    def __eq__(self, other):
        return self.titulo == other.titulo and self.autor == other.autor
    

    def __lt__(self, other):
        return self.autor < other.autor





#Pruebas para comprobar que funciona todo bien
libro1 = Libro("El Quijote", "Miguel de Cervantes", 5, 2)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 3, 1)

print(libro1)  #Imprime los datos del libro 1
print(libro2)  #Imprime los datos del libro 2

if (libro1.__eq__(libro2)):  #Compara los dos libros
    print("Los libros son iguales")
else:
    print("Los libros son diferentes")

libro1.prestamo()  #Realiza un préstamo del libro 1
print(libro1)  #Imprime los datos del libro 1 después del préstamo