''' 3. Nos piden hacer un programa que gestione una serie de productos. Los productos tienen los siguientes
atributos:
    a.Nombre
    b.Precio


Tenemos dos tipos de productos:
    a.Perecedero: tiene un atributo llamado días a caducar.
    b.No perecedero: tiene un atributo llamado tipo.


Tendremos una función llamada calcular, y que según la clase hará una cosa u otra. A esta función le pasaremos
un número que será la cantidad de productos:
    a.En Producto, simplemente sería multiplicar el precio por la cantidad de productos pasados y devolverá
    el resultado.
    b.En Perecedero, además de lo que hace producto, el precio se reducirá según los días a caducar:
        i. Si le queda 1 día para caducar, se reducirá 4 veces el precio final (dividir entre 4).
        ii. Si le quedan 2 días para caducar, se reducirá 3 veces el precio final (dividir entre 3).
        iii. Si le quedan 3 días para caducar, se reducirá a la mitad de su precio final (dividir entre 2).
    c.En NoPerecedero, hace lo mismo que en Producto.


Producto tiene que implementar los métodos __str__ y __lt__.  '''



class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


    def calcular(self, cantidad):
        return self.precio * cantidad
    

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}"

    def __lt__ (self, other):
        return self.precio < other.precio


class Perecedero(Producto):
    def __init__(self, nombre, precio, diasCaducar):
        super().__init__(nombre, precio)
        self.diasCaducar = diasCaducar
    
    def calcular(self, cantidad):
        if self.diasCaducar == 1:
            return super().calcular(cantidad)/4
        elif self.diasCaducar == 2:
            return super().calcular(cantidad)/3
        elif self.diasCaducar == 3:
            return super().calcular(cantidad)/2


    def __str__(self):
        return super().__str__()
    


class NoPerecedero(Producto):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo
    
    def calcular(self, cantidad):
        return super().calcular(cantidad)

    def __str__(self):
        return super().__str__()
    




#Pruebas
producto1 = Producto("Leche", 2)
producto2 = Perecedero("Yogur", 1.5, 2)
producto3 = NoPerecedero("Cerveza", 2, "Bebida")


print(producto1)
print(producto2)
print(producto3)

print(producto1.calcular(3))            #3 leches a 2 euros --> 6 euros
print(producto2.calcular(4))            #4 yogures a 1.5 euros, pero como caduca en 2 días, se divide entre 3  --> 2 euros
print(producto3.calcular(6))            #6 cervezas a 2 euros --> 12 euros