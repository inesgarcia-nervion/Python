'''9. Crea un diccionario donde las claves son las letras del abecedario y los valores, la puntuación
para cada letra, como en el Scrabble. El programa le pedirá una palabra al usuario y se mostrará por
pantalla la puntuación que tiene la palabra en total. '''


diccionario = {'a':1, 'b':3, 'c':2, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':6,
                'k':58, 'l':1, 'm':3, 'n':1, 'ñ':8, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1,
                'u':1, 'v':4, 'w':8, 'x':8, 'y':4, 'z':10}


palabra = input("Introduzca una palabra: ")
letra = palabra.split()
puntuacionTotal = 0


for letra in palabra:
    palabra = palabra.lower()
    if letra in diccionario:
        puntuacionTotal += diccionario[letra]
        print(f"La letra {letra} tiene {diccionario[letra]} puntos")
    else:
        print(f"La letra {letra} no está en el diccionario")




print(f"Enhorabuena! La palabra {palabra} tiene {puntuacionTotal} puntos")