def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse = key.setdefault(val, []).append[key]

    return inverse
