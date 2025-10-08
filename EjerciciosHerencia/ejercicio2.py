'''2. Codifica la siguiente jerarquía de clases java representada por este diagrama UML:


La clase base es la clase Empleado. Esta clase contiene:
    Un atributo privado nombre de tipo String.
    Un constructor por defecto.
    Un constructor con parámetros que inicializa el nombre con el String que recibe.
    Método set y get para el atributo nombre.
    Un método toString() que devuelve el String: "Empleado " + nombre.


El resto de clases sólo deben sobrescribir el método toString() en cada una de ellas y declarar el constructor
adecuado de forma que una vez creados objetos de cada una de las clases anteriores y tras imprimirlos por
pantalla el resultado sea:


    Empleado Rafa
    Empleado Mario --> Directivo
    Empleado Alfonso --> Operario
    Empleado Luis --> Operario --> Oficial
    Empleado Pablo --> Operario --> Técnico  '''



class Empleado:
    def __init__(self, nombre):      
        self._nombre = nombre           #Atributo privado
    
    def set_nombre(self, nombre):       #Setter
        self._nombre = nombre
    
    def get_nombre(self):               #Getter
        return self._nombre
    
    def __str__(self):
        return f"Empleado {self._nombre}"




class Directivo(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        return super().__str__() + " --> Directivo"
    
class Operario(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        return super().__str__() + " --> Operario"


class Oficial(Operario):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def __str__(self):
        return f"{super().__str__()} --> Oficial"           #Como también es operario, llamo al str de operario y añado oficial al final


class Tecnico(Operario):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def __str__(self):
        return f"{super().__str__()} --> Técnico"           #Como también es operario, llamo al str de operario y añado técnico al final







#Pruebas
empleado1 = Empleado("Rafa")
empleado2 = Directivo("Mario")
empleado3 = Operario("Alfonso")
empleado4 = Oficial("Luis")
empleado5 = Tecnico("Pablo")



print(empleado1)
print(empleado2)
print(empleado3)
print(empleado4)
print(empleado5)