long_string = "hello everybody"
words = ["hi", "everybody", "how", "are", "you"]

print(long_string[4])           # o
print(long_string[4:8])         # Desde la o hasta la v
print(long_string[2:12:2])      # De entre la letra en la posición 2 hasta el 12, coge las letras cada dos puestos
print(long_string.split())      # Divide como si fuera un array (si no hay nada en los paréntesis, es con espacio)

new_phrase = "-".join(words)    # Junta las palabras con un guión
print(new_phrase)



word1 = "hello".capitalize()    # Para mayúsculas
word2 = "hello"
print(len(word1))           # Cuanto mide
print(word1 < word2)        # Mayúscula es más grande
print(word1 == word2)       # Falso por las mayúsculas



long_string = "tenemos una cadena muy larga"
print(long_string[3:14:3])  # De entre la letra en la posición 3 hasta el 14, coge las letras cada tres puestos
print(long_string[::-1])    # Al revés