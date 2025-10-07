'''7. Realiza un programa que pida un número entero positivo y nos diga si es primo o no.'''
numero = int(input("Introduzca un número entero positivo: "))

esPrimo = True

if(numero <= 0):
   esPrimo = False
else:
   for i in range(2, numero):
      if numero % i == 0:    
         esPrimo = False
         break

if esPrimo:
   print("Es primo")
else:
   print("No es primo")
