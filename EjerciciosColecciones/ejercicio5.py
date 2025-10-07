import random

'''5. Crea un programa que cree una lista de enteros de tamaño 100 y lo rellene con valores enteros
aleatorios entre 1 y 10 (utiliza 1 + Math.random()*10). Luego pedirá un valor N y mostrará cuántas
veces aparece N. '''


lista = []

for i in range(100):
    aleatorioVeces = int(1 + random.random() * 10)        #No existe Math, por eso he usado random.random()
    lista.append(aleatorioVeces)


N = int(input("Introduzca un número entero: "))
cantidad = lista.count(N)
print(lista)


print("El número introducido se repite " + str(cantidad) + " veces")        #Se pasa a string para que se pueda concatenar
