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
