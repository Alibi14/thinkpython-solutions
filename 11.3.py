known = {}


# memorize ackerman function
def ack(m, n):
    if m == 0:
        for_m = n+1
        known[m] = for_m
        return for_m
    elif m > 0 and n == 0:
        a = ack(m - 1, 1)
        known[m] = a
        return a
    elif m > 0 and n > 0:
        res = ack(m - 1, ack(m, n - 1))
        known[m, n] = res
        return res


print(ack(3, 4))
print(known)