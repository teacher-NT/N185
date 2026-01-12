import os 
os.system("cls")

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

class Student(Person):
    def __init__(self, grade, name, age):
        super().__init__(name, age)
        self.grade = grade

baxo = Student(80, "Bexruz", 21)
print("Ism:", baxo.name)
print("Yoshi:", baxo.age)
print("Baxosi:", baxo.grade)