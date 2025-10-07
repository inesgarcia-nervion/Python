import random

'''4. Codificar el juego “el número secreto”, que consiste en acertar un número entre 1 y 100 (generado aleatoriamente).
Para ello se introduce por teclado una serie de números, para los que se indica: “mayor” o “menor”, según sea mayor o menor
con respecto al número secreto. El proceso termina cuando el usuario acierta o cuando se rinde (introduciendo un -1).'''
aleatorio = random.randint(1, 100)

while True:
   adivinar = int(input("Introduzca un número entre el 1 y el 100: "))

   if adivinar == -1:
      print("Que pena! El número era ", aleatorio)
      break
   elif adivinar == aleatorio:
      print("El número era: ", aleatorio)
      break
   elif adivinar > aleatorio:
      print("El número es más menor")
   elif adivinar < aleatorio: 
      print("El número es más mayor")
   else:
      print("Introduzca un número entre el 1 y el 100") 