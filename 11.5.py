from rotate import rotate_word


fin = open('words.txt')


def make_word_dict():
    d = {}

    for line in fin:
        words = line.strip().lower()
        if words not in d:
            d[words] = True

    return d


word_dict = make_word_dict()


def rotate_pairs(word, word_dict):
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print(word, i, rotated)


for word in word_dict:
    rotate_pairs(word, word_dict)



