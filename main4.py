import os
os.system("cls")

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound

nmadr = Dog("Bobik", "wooof")
print("Nomi:", nmadr.name)
print("Ovozi:", nmadr.sound)