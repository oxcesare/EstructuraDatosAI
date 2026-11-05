numero =10

def funcion1():
     global numero 
     numero += 20
     print("El numero es: ", numero)


def funcion2():
     global numero 
     numero += 40
     print("El numero es: ", numero)

funcion1()
funcion2()
