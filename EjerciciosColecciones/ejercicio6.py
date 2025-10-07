'''6. Escribe un programa que tome una cadena de texto como entrada y genere un diccionario que cuente
la frecuencia de cada palabra en el texto. '''

diccionario = {}


texto = input("Introduzca una cadena de texto: ")
palabras = texto.split()


for i in palabras:
    if i in diccionario:
        diccionario[i] += 1             #Entra en el diccionario y suma 1
    else:
        diccionario[i] = 1              


for i, count in diccionario.items():
    print(f"La palabra {i} se repite {count} veces")  