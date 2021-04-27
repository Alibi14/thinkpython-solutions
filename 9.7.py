fin = open('words.txt')


def consequetive(word):
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                return True
            i = i + 2
        else:
            i = i + 1 - 2 * count
            count = 0

    return False


for line in fin:
    word = line.strip()
    if consequetive(word):
        print(word)