def has_duplicates(t):
    d = {}

    for x in t:
        if x in d:
            print(d)
            return True
        d[x] = True
    print(d)
    return False


print(has_duplicates('aa'))