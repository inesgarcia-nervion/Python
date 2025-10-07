word1 = "hello"
word2 = "everybody"

a = 3
b = 8

if a == b:
    print("They are equals")
    print("end of the program") # IMPORTANTE usar tabulador y no espacio (si no lo hace automático). Si quitas el tabulador de este, se imprime la frase (end of the program)
else:
    print("There are not the same")



if a < b:
    print(a,b)
elif a > b:
    print(b,a)
else:
    print(a,b)



resul = "even" if a%2==0 else "odd"     # El número es impar
print(resul)