''' 1. Crea con un editor el fichero de texto Alumnos.txt y escribe en él los nombres, edades y estaturas
de los alumnos de un grupo, cada uno en una línea:
    juan 22 1.77
    luis 21 1.80
    pedro 20 1.73
    …
Implementa un programa que lea del fichero los datos, muestre los nombres y calcule la media de la edad
y de las estaturas, mostrándolas por pantalla.   '''



with open('Alumnos.txt', 'w', encoding="utf8") as w:   #Se escriben los datos
    w.write("juan 22 1.77 \n")
    w.write("luis 21 1.80 \n")
    w.write("pedro 20 1.73 \n")


calcularEdad = 0
calcularEstatura = 0
totalAlumnos = 0


with open('Alumnos.txt', 'r', encoding="utf8") as r:        #Se leen los datos
    for linea in r:
        separacion = linea.split()
        nombre = separacion[0]
        edad = int(separacion[1])
        estatura = float(separacion[2])

        print(nombre)                           #Hay que imprimir los nombres dentro del bucle

        calcularEdad += edad
        calcularEstatura += estatura
        totalAlumnos += 1

mediaEdad = calcularEdad / totalAlumnos
mediaEstatura = calcularEstatura / totalAlumnos

print(f'La media de edad de los alumnos es de {mediaEdad} ')
print(f'La media de la estatura de los alumnos es de {mediaEstatura} ')



