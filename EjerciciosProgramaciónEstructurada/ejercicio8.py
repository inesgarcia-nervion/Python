'''8. Solicita al usuario un número n y dibuja un triángulo de base y altura n. Por ejemplo para n=4 debe dibujar lo siguiente:
   *
  * *
 * * *
* * * *'''
numero = int(input("Introduzca un número entero positivo: "))

for i in range(1, numero + 1):
    print(" " * (numero - i), " * " * i) 