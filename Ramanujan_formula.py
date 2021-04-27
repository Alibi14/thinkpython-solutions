import math


def factorial(n):
    if n == 0:
        return 1
    else:
        a = n * factorial(n-1)
        return a


def ramanujan():
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        upper = factorial(4 * k) * (1103 + 26390 * k)
        under = math.pow(factorial(k), 4) * (math.pow(396, 4 * k))
        term = upper/under
        total += + term
        if abs(term) < 1e-15:
            break
        k += 1

    return 1 / total


print(ramanujan())

