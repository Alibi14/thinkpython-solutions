def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_polindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    print(middle(word))
    print('space')
    return is_polindrome(middle(word))


print(is_polindrome('redivider'))
