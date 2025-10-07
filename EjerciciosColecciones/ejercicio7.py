'''7. Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una libreta
de direcciones implementada como un diccionario. La clave del diccionario será el nombre del contacto
y el valor, su número de teléfono. Crea un menú para las distintas opciones e implementa una función
para cada opción. '''


diccionario = {}


#Funciones
def agregar():
    nombre = input("Introduzca el nombre que quiera agregar: ")                 #Key
    if nombre in diccionario:
        print(f"El contacto {nombre} ya existe en el teléfono")
    else:
        telefono = int(input("Introduzca el teléfono que quiera agregar: "))        #Value
        diccionario[nombre] = telefono


def eliminar():
    nombre = input("Introduzca el nombre que quiera eliminar: ")    
    if nombre in diccionario:
        diccionario.pop(nombre)
        print(f"El contacto {nombre} ha sido eliminado")
    else:
        print(f"No se ha encontrado el contacto {nombre}")



def buscar():
    nombre = input("Introduzca el nombre que quiera buscar: ")
    if nombre in diccionario:
        telefono = diccionario.get(nombre)
        print(f"Este es el contacto {nombre} y su teléfono {telefono} ")
    else:
        print(f"No se ha encontrado el contacto {nombre}")




#Menú
stop = True




while(stop):
    menu = int(input("Que quiere realizar: 1.Agregar, 2.Eliminar, 3.Buscar contactos, -1.Salir del programa: "))
    match menu:
        case 1:
            agregar()
            print(diccionario)
        case 2:
            eliminar()
            print(diccionario)
        case 3:
            buscar()
            print(diccionario)
        case -1:
            stop = False                        #Para salir del bucle
            print("Saliendo del programa")      
        case _:
            print("Introduzca el número solicitado")