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
    def __init__(self, dni, saldo_inicial, nombre=""):     #Constructores (nombre tiene que estar vacio)
        self.dni = dni
        self.saldo = saldo_inicial
        self.nombre = nombre

    
    def sacarDinero(self, cantidad):  #Método para sacar dinero
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        else:
            return False
        
        
    def ingresarDinero(self, cantidad):    #Método para ingresar dinero
        if cantidad >  0:
            self.saldo += cantidad
            return True
        else:
            return False
    

    def __str__(self):  #Método str
        return f"DNI: {self.dni}, Nombre: {self.nombre}, Saldo: {self.saldo}"
    
    def __eq__(self, other): #Método eq
        return self.dni == other.dni