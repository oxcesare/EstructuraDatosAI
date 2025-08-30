class Gato:
    def hacer_sonido(self):
        return "Miau"
    
class Perro:
    def hacer_sonido(self):
        return "Guau"

def hacer_sonido_animal(animal):
    print (f"El sonido del animal es: {animal.hacer_sonido()}")      

hacer_sonido_animal(Gato())
hacer_sonido_animal(Perro())