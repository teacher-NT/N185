import os
os.system("cls")

class BankAccount:
    def __init__(self, n, b):
        self.name = n
        self.__balans = b

    def get_balans(self, parol):
        if parol == "1234":
            return self.__balans
        else:
            return "Parol xato!"
    
    def set_balans(self, qiymat, parol):
        if parol == "1234":
            self.__balans = qiymat
        else:
            print("Parol xato!")
    

b1 = BankAccount("Ruslan", 1000)
# b1.name = "Abdulla"
print(b1.name)
b1.set_balans(2500, "1234")
print(b1.get_balans("1234"))