'''9. Escribe una función a la que se le pasen dos enteros y muestre todos los números comprendidos entre ellos. Desde el método main()
lee los dos números enteros, los cuales deben introducirlos el usuario, y pásalos como parámetros de entrada de la función.'''
numero1 = int(input("Introduzca un número entero: "))
numero2 = int(input("Introduzca otro número entero: "))

for i in range(numero1 + 1, numero2):
    print(i)
