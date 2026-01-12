import os
os.system("cls")

class Transport:
    def __init__(self, o_k, rang, brand, model, narx):
        self.o_k = o_k
        self.rang = rang
        self.brand = brand
        self.model = model
        self.narx = narx

    def move(self):
        print("Transport harakatlanmoqda...")


class Car(Transport):
    pass

class Plane(Transport):
    pass

car1 = Car(500, "Oq", "BMW", "M5", 128000)
car1.move()

plane1 = Plane(800, "Qora", "Boing", "&45", 20_000_000)
plane1.move()