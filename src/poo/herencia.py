class Animal:
    def comer(self):
        print("El animal está comiendo.")

class Perro(Animal):
    def ladrar(self):
        print("El perro está ladrando.")

p = Perro()
p.comer()
p.ladrar()

