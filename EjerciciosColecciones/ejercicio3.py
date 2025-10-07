'''3. Realiza un programa que pida 8 números enteros y los almacene en una lista. A continuación,
recorrerá esa tabla y mostrará esos números junto con la palabra “par” o “impar” según proceda. '''

lista = []


for i in range(8):
    paroimpar = int(input("Introduzca un número entero: "))
    lista.append(paroimpar)



for paroimpar in lista:
    resultado = "par" if paroimpar%2==0 else "impar"
    print(f"{paroimpar} {resultado}")


print(f"Lista completa: {lista}")