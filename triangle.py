import math

def is_triangle(a,b,c):
    if a + b < c:
        print("it can't be the triangle")
    else:
        print("it can!")


def checking_is_triangle():
    a = int(input("please input a: "))
    b = int(input("please input b: "))
    c = int(input("please input c: "))
    is_triangle(a,b,c)

checking_is_triangle()

