'''2. Crea una clase llamada Libro que guarde la información de cada uno de los libros de una biblioteca.
La clase debe guardar el título del libro, autor, número de ejemplares del libro y número de ejemplares prestados.
La clase contendrá los siguientes métodos:


    a.Constructor con todos los parámetros (se le indica valores para todos los atributos).
    b.prestamo(): incrementa el atributo correspondiente cada vez que se realice un préstamo.
    No se pueden prestar libros si no quedan ejemplares disponibles para prestar. Devuelve true si se ha
    podido realizar el préstamo y false en caso contrario.
    c.devolucion(): decrementa el atributo correspondiente cada vez que se devuelva un libro. No se podrán
    devolver libros que no se hayan prestado. Devuelve true si se ha podido realizar la operación y false en
    caso contrario.
    d.Crear también los métodos __str__, __eq__ y __lt__. Se considera que dos  libros son iguales si tienen
    el mismo título y el mismo autor. Los libros se ordenarán de menor a mayor por el nombre del autor. '''
