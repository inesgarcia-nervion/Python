'''4. Escribe un programa que lea 10 números por teclado y que luego los muestre ordenados de mayor a menor.'''

lista = []


for i in range(10):
    mayoramenor = int(input("Introduzca un número entero: "))
    lista.append(mayoramenor)


lista.sort(reverse=True)      #Ordena los números de mayor a menor (por defecto sort ordena de menor a mayor)


print(lista)