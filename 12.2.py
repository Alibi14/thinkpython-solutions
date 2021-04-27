def signature(word):

    t = list(word)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams():
    d = {}
    fin = open('words.txt')

    for line in fin:
        word = line.strip().lower()
        word = list(word)
        t = signature(word)
        if t not in d:
            d[t] = word
        else:
            d[t].append(word)

    new_var = d.items()
    return new_var


print(all_anagrams())