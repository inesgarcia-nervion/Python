'''1. Diseñar la clase CuentaCorriente, que almacena los datos DNI, nombre y el saldo.
Añade los siguientes constructores:
    a.Con el DNI del titular de la cuenta y un saldo inicial. El nombre se inicializará a cadena vacía.
    b.Con el DNI, nombre y el saldo inicial.


    Las operaciones típicas de una cuenta corriente son:
    a.Sacar dinero: el método debe indicar si ha sido posible llevar a cabo la operación, si existe saldo
    suficiente. Si es posible llevar a cabo la operación se resta la cantidad a sacar al saldo de la cuenta.
    b.Ingresar dinero: se incrementa el saldo.
    c.Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos cuentas corrientes son iguales
    si tienen el mismo DNI. Las cuentas corrientes se ordenarán de menor a mayor por el saldo. '''

class CuentaCorriente:
    def __init__(self, dni, saldoInicial, nombre):     #Constructores (con todos los parámetros)
        self.dni = dni
        self.saldoInicial = saldoInicial
        self.nombre = nombre

    def __init__(self, dni, saldoInicial):     #Constructores (nombre tiene que estar vacio)
        self.dni = dni
        self.saldoInicial = saldoInicial
        self.nombre = ""

    def sacarDinero(self, cantidad):  #Método para sacar dinero
        if cantidad <= self.saldoInicial:
            self.saldoInicial -= cantidad
            return True
        else:
            return False
        
        
    def ingresarDinero(self, cantidad):    #Método para ingresar dinero
        if cantidad >  0:
            self.saldoInicial += cantidad
            return True
        else:
            return False
    

    def __str__(self):  #Método str para imprimir los datos de la cuenta
        return f"DNI: {self.dni}, Nombre: {self.nombre}, Saldo: {self.saldoInicial}"
    

    def __eq__(self, other): #Método eq para comparar los DNI de dos cuentas
        return self.dni == other.dni
    

    def __lt__(self, other): #Método lt para ordenar las cuentas por saldo
        return self.saldoInicial < other.saldoInicial
    





#Pruebas para comprobar que funciona todo bien
cuentaCorriente1 = CuentaCorriente("12345678A", 1000, "Juan Perez") 
cuentaCorriente2 = CuentaCorriente("87654321B", 500, "Maria Gomez")

print(cuentaCorriente1)  #Imprime los datos de la cuenta 1
print(cuentaCorriente2)  #Imprime los datos de la cuenta 2

if (cuentaCorriente1.__eq__(cuentaCorriente2)):  #Compara las dos cuentas
    print("Las cuentas son iguales")
else:
    print("Las cuentas son diferentes")

if (cuentaCorriente1.__lt__(cuentaCorriente2)):  #Compara las dos cuentas por saldo
    print("La cuenta 1 tiene menos saldo que la cuenta 2")
else:
    print("La cuenta 1 tiene más saldo que la cuenta 2")