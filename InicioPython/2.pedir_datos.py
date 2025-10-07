user_name=input("Introduce your name: ")
print("Your name is", user_name)        # La coma también realiza un espacio



age = int (input("Introduce your age: "))       # Hay que castear a número entero porque no puede sumar un String (si le ponemos comillas, si deja pero como cadena (231))
age+=1              # No existe el ++


print("Your age is:", age)
##print("Your age is:" + age)              Error porque el + solo funciona con cadena (es de tipo entero)
print(f"Your age is: {age}")               # Formateo de la cadena




# Comentario corto
'''
Comentario largo
'''