''' 2.Crea un programa en python que cree un fichero en modo escritura. A continuación, irá leyendo línea
a línea de teclado hasta que el usuario introduzca la cadena “fin”. Debe escribir cada línea en el fichero
creado. '''

fin = False
listaCompleta = ""

    
while not fin:
    palabras = input("Introduzca palabras al azar (Escriba fin cuando quiera dejar el programa): ")
    if palabras.lower() == "fin":
        print("Fin del programa")
        fin = True
        
    else:
        listaCompleta += palabras + "\n"


with open('Palabras.txt', 'w', encoding="utf8") as w:   #Se escriben los datos
    w.write(listaCompleta)
    print(listaCompleta)