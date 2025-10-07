'''10. Crea un diccionario donde las claves sean el conjunto 1 de la siguiente tabla y los valores,
el conjunto 2:




conjunto 1: e i k m p q r s t u v
conjunto 2: p v i u m t e r k q s




El programa debe pedir una frase al usuario y debe mostrar la frase encriptada. Para ello, cada
vez que encuentre en la frase una letra del conjunto 1 la sustituirá por su correspondiente en
el conjunto 2.  '''




##Ejemplo: conjunto 1: meru  --> conjunto 2: upeq




diccionario = {'e': 'p', 'i': 'v', 'k': 'i', 'm': 'u', 'p': 'm', 'q': 't', 'r': 'e', 's': 'r', 't': 'k', 'u': 'q', 'v': 's'}


frase = input("Introduzca una frase: ")
resultado = ""


letra = frase.split()


for letra in frase:
    letra = letra.lower()
    if letra in diccionario:
        resultado += diccionario[letra]
        print(diccionario[letra])
    else:
        print(letra)




print(f"La frase encriptada es {resultado}")
