'''8. Diseña un programa que registre las ventas de una tienda en un diccionario, donde las claves son
los nombres de los productos y los valores son las cantidades vendidas. El programa debe permitir al
usuario agregar nuevas ventas y calcular el total de ventas para un producto específico.
Implementa un menú con ambas opciones. '''
diccionario = {}


def agregar():
    producto  = input("Introduzca el nombre del producto que quiera agregar: ")                 #Key
    if producto in diccionario:
        print(f"El producto {producto} ya existe en la tienda")
    else:
        cantidad = int(input("Introduzca la cantidad vendida del producto: "))        #Value
        diccionario[producto] = cantidad




def aumentar():
    producto = input("Introduzca el nombre del producto al que le quiera aumentar la venta: ")
    if producto in diccionario:
        cantidad = int(input("Introduzca la cantidad vendida del producto: "))
        diccionario[producto] += cantidad
    else:
        print(f"No se ha encontrado el producto {producto}")




def total():
    producto = input("Introduzca el nombre del producto que quiera consultar: ")
    if producto in diccionario:
        cantidad = diccionario.get(producto)
        print(f"El total de vental del producto {producto} es {cantidad}")
    else:
        print(f"No se ha encontrado el producto {producto}")
   


#Menú
stop = True


while(stop):
    menu = int(input("Que quiere realizar: 1.Agregar venta, 2.Aumentar productos existentes 3.Consultar total de ventas, -1.Salir del programa: "))
    match menu:
        case 1:
            agregar()
            print(diccionario)
        case 2:
            aumentar()
            print(diccionario)
        case 3:
            total()
            print(diccionario)
        case -1:
            stop = False
            print("Saliendo del programa")