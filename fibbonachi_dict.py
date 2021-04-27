known = {0:0, 1:1}


def fibbonachi(n):
    if n in known:
        return known[n]

    res = fibbonachi(n-1) + fibbonachi(n-2)
    known[n] = res
    print(known)
    return res


fibbonachi(5)