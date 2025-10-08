''' 1. Crea con un editor el fichero de texto Alumnos.txt y escribe en él los nombres, edades y estaturas
de los alumnos de un grupo, cada uno en una línea:
    juan 22 1.77
    luis 21 1.80
    pedro 20 1.73
    …
Implementa un programa que lea del fichero los datos, muestre los nombres y calcule la media de la edad
y de las estaturas, mostrándolas por pantalla.   '''



f = open('Alumnos.txt', 'w', encoding="utf8")   #Para que se vean las tildes
f.write("juan 22 1.77 \n")
f.write("luis 21 1.80 \n")
f.write("pedro 20 1.73 \n")



class Alumno:
    def __init__(self, nombre, edad, estatura):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
    
    def leerNombres(self):
        alumnos = []
        f = open('Alumnos.txt', 'w', encoding="utf8")
        for linea in f:
            letras = linea.split()


