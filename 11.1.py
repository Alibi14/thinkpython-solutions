fin = open('words.txt')


def reads_words():
    dictionary = dict()
    count = 0
    for line in fin:
        words = line.strip()
        dictionary[words] = count
        count += 1

    print(dictionary)
    return dictionary


reads_words()