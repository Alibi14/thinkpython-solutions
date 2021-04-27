def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False


print(has_match('ali', 'aua'))

