'''12. Diseñar la función calculadora(), a la que se le pasan dos números reales (operandos) y qué operación se desea realizar con ellos. 
Las operaciones disponibles son sumar, restar, multiplicar o dividir. Estas se especifican mediante un número: 1 para la suma, 2 para la resta, 3 para
la multiplicación y 4 para la división. La función devolverá el resultado de la operación mediante un número real.'''
def calculadora(numero1, numero2, operacion):
   match operacion:
      case 1:
         return numero1 + numero2
      case 2:
         return numero1 - numero2
      case 3:
         return numero1 * numero2
      case 4:
         return numero1 / numero2
      case _:
         return print("Operación no válida")
   

numero1 = float(input("Introduzca un número entero: "))
numero2 = float(input("Introduzca otro número entero: "))

operacion = int(input("1 para la suma, 2 para la resta, 3 para la multiplicación y 4 para la división: "))

resultado = calculadora(numero1, numero2, operacion)

print("El resultado es ", resultado)