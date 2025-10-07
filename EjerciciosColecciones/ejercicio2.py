'''2. Crea un programa que pida diez números reales por teclado, los almacene en una lista, y
luego lo recorra para averiguar el máximo y mínimo y mostrarlos por pantalla. '''

lista = []


for i in range(10):
    maxomin = float(input("Introduzca un número entero: "))
    lista.append(maxomin)


maximo = max(lista)
minimo = min(lista)


print(f"El máximo es: {maximo} " + f" y el mínimo es: {minimo}")
