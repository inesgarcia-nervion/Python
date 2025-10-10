''' 1. Crea con un editor el fichero de texto Alumnos.txt y escribe en él los nombres, edades y estaturas
de los alumnos de un grupo, cada uno en una línea:
    juan 22 1.77
    luis 21 1.80
    pedro 20 1.73
    …
Implementa un programa que lea del fichero los datos, muestre los nombres y calcule la media de la edad
y de las estaturas, mostrándolas por pantalla.   '''



with open('Alumnos.txt', 'w', encoding="utf8") as f:   #Para que se vean las tildes
    f.write("juan 22 1.77 \n")
    f.write("luis 21 1.80 \n")
    f.write("pedro 20 1.73 \n")




edadTotal = 0
estaturaTotal = 0
cantidadAlumnos = 0



print('Nombre de los alumnos: ')        #Para que no entre en el bucle


with open('Alumnos.txt', 'r', encoding="utf8") as f:
    for linea in f.readlines():
        separacion = linea.split()
        nombre = separacion[0]
        edad = int(separacion[1])
        estatura = float(separacion[2])

        edadTotal += edad
        estaturaTotal += estatura
        cantidadAlumnos += 1

        print(nombre)                   #Para imprimir cada nombre de manera individual



mediaEdad = edadTotal / cantidadAlumnos
mediaEstatura = estaturaTotal / cantidadAlumnos

print(f'La edad media de los alumnos es de {mediaEdad} años')
print(f'La estatura media de los alumnos es de {mediaEstatura} metros')