'''4. Implementa un programa que lea números enteros no ordenados de un archivo, 
con un número por línea, y los almacene en una lista. A continuación, debe guardar 
los números de la lista en otro fichero distinto pero ordenados de forma ascendente. '''


with open ('desordenado', 'w', encoding="utf8") as w:           #Primero creamos una lista con los números desordenados
    w.write("2\n")
    w.write("3\n")
    w.write("1\n")


with open ('desordenado', 'r', encoding="utf8") as r:           #A continuación, lee los datos, se crea la lista y se guardan
    numeros = []
    for linea in r:
        numeros.append(int(linea.strip()))

numeros.sort()                                                  #Se ordenan los números de dentro de la lista

with open ('ordenado', 'w', encoding="utf8") as w:              #Por último, se escriben los números ordenados en un fichero nuevo
    w.write(f"{numeros}\n")