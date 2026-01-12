import os
os.system("cls")

class Flyable:
    def fly(self):
        print("Uchmoqda...")

class Swimable:
    def swim(self):
        print("Suzmoqda...")

class Duck(Flyable, Swimable):
    def eat(self):
        print("Ovqatlanmoqda...")

d1 = Duck()
d1.fly()
d1.swim()
d1.eat()