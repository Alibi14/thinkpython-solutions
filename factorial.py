import math


def factorial(n):
    if not isinstance(n, int):
        print("This function will accept only integers")
        return None
    elif n < 0:
        print("This function will accept only positive numbers")
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(6))
