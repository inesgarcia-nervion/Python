'''4. Crea una clase llamada Articulo con los siguientes atributos: nombre, precio (sin IVA), iva
(siempre será 21) y cuantosQuedan (representa cuántos quedan en el almacén). Añade los siguientes métodos:


    a.Constructor con 3 parámetros que asigne valores a nombre, precio y cuantosQuedan. El IVA siempre lo
    pondrá a 21.
    b.Método getPVP que devuelva el precio de venta al público (PVP) con iva incluido.
    c.Método getPVPDescuento que devuelva el PVP con un descuento pasado como argumento.
    d.Método vender que actualiza los atributos del objeto tras vender una cantidad ‘x’ (si es posible).
    Devolverá true si ha sido posible (false en caso contrario). La cantidad a vender se pasará como argumento
    al método.
    e.Método almacenar que actualiza los atributos del objeto tras almacenar una cantidad ‘x’.
    La cantidad a almacenar se pasará como argumento.
    f.Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos artículos son iguales si
    tienen el mismo nombre. Los artículos se ordenarán de menor a mayor por el nombre.  '''

class Articulo:

    iva = 21

    def __init__(self, nombre, precio, cuantosQuedan):
        self.nombre = nombre
        self.precio = precio
        self.cuantosQuedan = cuantosQuedan


    def getPVP(self, iva):
        return self.precio * Articulo.iva / 100 + self.precio


    def getPVPDescuento(self, descuento):
        return self.getPVP(self.iva) * (1 - descuento / 100)
    

    def vender(self, cantidad):
        if cantidad <= self.cuantosQuedan:
            self.cuantosQuedan -= cantidad
            return True 
        else:
            return False
        
    def almacenar(self, cantidad):
        self.cuantosQuedan += cantidad
        return self.cuantosQuedan
   
    

    def __str__(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Cuantos quedan: {self.cuantosQuedan}"


    def __eq__(self, other):
        return self.nombre == other.nombre
    

    def __lt__(self, other):
        return self.nombre < other.nombre





#Pruebas para comprobar que funciona todo bien
producto1 = Articulo("Camiseta", 20, 50)
producto2 = Articulo("Pantalon", 40, 6)


print(producto1) 
print(producto2)  


print(producto1.getPVP(Articulo.iva))
print(producto1.getPVPDescuento(10))
print(producto2.vender(10))                     #False porque hay menos pantalones que los que se quieren vender
print(producto2.almacenar(20))