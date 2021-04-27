def make_histogram(s):
    hist = {}

    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


def most_frequent(s):
    d = make_histogram(s)

    t = []

    for x, freq in d.items():
        t.append((freq, x))

    t.sort(reverse=True)

    res = []

    for freq, x in t:
        res.append(x)

    return res


print(most_frequent('elementary'))


