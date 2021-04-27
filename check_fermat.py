import math

def check_fermat(a,b,c,n):
    if n > 2 and (math.pow(a, n) + math.pow(b, n)) == math.pow(c, n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")

check_fermat(2,2,3,3)

def check_fermat_custom():
    a = int(input("please input a: "))
    b = int(input("please input b: "))
    c = int(input("please input c: "))
    n = int(input("please input n: "))
    check_fermat(a,b,c,n)

check_fermat_custom()