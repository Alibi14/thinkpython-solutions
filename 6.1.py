def a(x, y):
    x = x + 1
    print(x * y)
    return x * y


def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod


def c(x, y, z):
    total = x + y + z
    square = b(total) ** 2
    print(square)
    return square
    x = 1
    y = x + 1
    print(c(x, y + 3, x + y))


c(2, 3, 4)

