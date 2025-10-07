import random


'''1. Crea una lista de enteros de longitud 10 que se inicializará con números aleatorios comprendidos
entre 1 y 100. '''

lista = []

for contador in range (10):
    aleatorio = random.randint(1, 100)
    lista.append(aleatorio)

print(lista)