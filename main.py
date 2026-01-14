import os
os.system("cls")

class Person:
    def __init__(self, ism,yosh,jins,manzil):
        self.ism = ism
        self.yosh = yosh
        self.jins = jins
        self.manzil = manzil
    
    def __str__(self):
        return f"Ism: {self.ism}. Yosh: {self.yosh} {self.jins} {self.manzil}"
    
    def __gt__(self, n):
        return self.yosh > n
    
class Employee:
    def __init__(self, ism, yosh, jins, manzil, tajriba, maosh):
        self.ism = ism
        self.yosh = yosh
        self.jins = jins
        self.manzil = manzil
        self.tajriba = tajriba
        self.maosh = maosh

    def __str__(self):
        return f"Ism: {self.ism}. {self.manzil} {self.maosh}"

    def __gt__(self, n):
        return self.maosh > n



p1 = Person("Abdulla", 15, "Erkak", "Toshkent sh.")
e1 = Employee("Vali", 21, "Erkak", "Qo'qon", 3, 500)

print(p1 > 20)
print(e1 > 20)