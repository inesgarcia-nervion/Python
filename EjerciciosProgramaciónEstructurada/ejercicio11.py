'''11. Crear una función que devuelva un tipo booleano que indique si el carácter que se pasa como parámetro de entrada corresponde con una vocal.'''
letra = input("Introduzca una vocal: ")
vocal = ['a','e','i','o','u','A','E','I','O','U']

if letra in vocal:
    print("Es una vocal")
else: 
    print("Es una consonante")