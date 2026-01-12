import os 
os.system("cls")

class A:
    def func(self):
        print('Men A classdanman')

class B(A):
    pass
    
class C(B):
    pass

# b1 = B()
# b1.func()

c1 = C()
c1.func()