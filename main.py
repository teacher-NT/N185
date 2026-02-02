import os
os.system("cls")

class Car:
    def __init__(self, b,m,n,r):
        self.brand = b
        self.model = m
        self.narx = n   
        self.rang = r

    def info(self):
        print(f"{self.brand} {self.model} {self.rang} {self.narx}")

    def show_price(self):
        print(self.narx)

    def change_price(self, n):
        if n < 20000:
            print("Narx 20000dan kichik bo'lmasin")
        else:
            self.narx = n

c1 = Car("BMW", "M5", 120000, "qora")

# c1.narx = 25000
c1.change_price(100000)
c1.info()

c2 = Car("Chevrolet", "Spark", 6000, "oq")
c2.info()

car3 = Car("Chevrolet", "Damas", 6000, "oq")
car3.info()

# print(c1.brand)
# print(c1.narx)





# a = 12
# b = 2.3
# d = "Salom"
# e = True

# print(type(a))
# print(type(b))
# print(type(d))
# print(type(e))
# print(type(c1))
