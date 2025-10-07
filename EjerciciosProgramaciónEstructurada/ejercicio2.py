'''2. Pedir dos números y mostrarlos ordenados de menor a mayor. '''
numero1 = int(input("Introduzca un número: "))
numero2 = int(input("Introduzca otro número: "))
mayor = numero1 if numero1 > numero2 else numero2
menor = numero1 if numero1 < numero2 else numero2
print(menor, mayor)