import os
os.system("cls")

class A:
    def run(self):
        print("A is runing...")

class B(A):
    def run(self):
        print("B is runing...")

class C(A):
    def run(self):
        print("C is runing...")

class D(B,C,A):
    pass

print(D.mro())


# class E(D, C):
#     pass

# e1 = E()
# e1.run()
# d1 = D()
# d1.run()