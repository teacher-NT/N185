import os
os.system("cls")

class Car:
    def __init__(self, brand, model, rang, narx):
        self.brand = brand
        self.model = model
        self.rang = rang
        self.narx = narx
    
    def __str__(self):
        return f"{self.brand} - {self.model}"
    
    def __add__(self, n):
        self.narx += n
        print("add metodi ishladi")
    
    def __sub__(self, n):
        self.narx -= n

    def __gt__(self, n):
        return self.narx > n
    
    def __lt__(self, n):
        return self.narx < n
    


car1 = Car("GM", "Nexia", "Oq", 15000)
car1 + 10
car1 - 500

print(car1 < 1000)
print(car1 > 1000)