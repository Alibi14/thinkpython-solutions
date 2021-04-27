def is_reverse(w1, w2):
    if len(w1) != len(w2):
        return False

    i = 0

    j = len(w2) - 1

    while j > 0:
        print(j)
        print(i, " this is i")
        if w1[i] != w2[j]:
            return False

        i += 1
        j -= 1

    return True


def middle(word):
    return word[1:-1]


print(middle("alibi"))
