import os
os.system("cls")

# =======================================================
# for i in range(10, 20, 2):
#     print(i)

# def func1(*args):
#     print(args)
#     # s = 0
#     # for i in m:
#     #     s += i
#     s = sum(args)
#     print(s)

# func1(1,2)

# ========================================================
def func2(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k,v)

# func2(ism="Alisher", yosh=19, vazn=66.5)

# =======================================================

def func3(a,b):
    print((a+b)/2)
# func3(4,6)

func4 = lambda a,b: print((a+b)/2)
# func4(4,6)

# ========================================================

lst = [10,90,85,70,25,36,44,59,60]

def func5(n):
    return n>=60
res = list(filter(func5, lst))
# print(res)

ages = [14,20,16,15,14,18,20,14,22,15,20,18,18]
def func6(n):
    return n+1
res = list(map(func6, ages))
# print(res)