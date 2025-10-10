''' 3. Diseña una aplicación que pida al usuario su nombre y edad. Estos datos deben 
guardarse en el fichero datos.txt. Si este fichero existe, deben añadirse al final 
en una nueva línea, y en caso de no existir, debe crearse. '''


nombre = input("Introduzca su nombre: ")
edad = int(input("Introduzca su edad: "))


with open ('datos.txt', 'a', encoding="utf8") as a:         #Abriendo el archivo con append, nos añade los datos si el fichero existe y sino lo crea
    a.write(f'Nombre: {nombre} , Edad: {edad} \n' )