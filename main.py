import os
os.system("cls")

class Product:
    def __init__(self, n, p, s, w, t):
        self.name = n
        self.price = p
        self.shelf_life = s
        self.weight = w
        self.type_fruit = t

    def info(self):
        print(f"Maxsulot: {self.name}, Narxi: {self.price}")
    
    def discount(self, foiz):
        # self.price = self.price-(self.price/100*foiz)
        self.price -= self.price/100*foiz
    
    def increase_price(self, foiz):
        self.price = self.price+(self.price/100*foiz)


p1 = Product("Yogurt", 12000, '1-oy', 500, 'Banan')
p1.info()
p1.discount(30)
p1.info()
p1.increase_price(50)
p1.info()
