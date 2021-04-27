def rotate_letter(letter, n):
    if letter.isupper():
        start = ord('A')
    else:
        start = ord('a')

    c = ord(letter) - start

    i = (c + n) % 26 + start

    return chr(i)


def rotate_word(word, n):
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res


print(rotate_word('cheer', 7))