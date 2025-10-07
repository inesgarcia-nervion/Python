'''6. Pedir un número y calcular su factorial. Por ejemplo, el factorial de 5 se denota 5! y es igual a 5x4x3x2x1 = 120.'''
numero = int(input("Introduzca un número entero: "))
resultado = 1

for i in range(1, numero + 1):
    resultado *= i


print("El resultado del factorial de", numero, "es", resultado)