def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        print(gcd_recursive(b, a % b))
        return gcd_recursive(b, a % b)


gcd_recursive(14, 16)