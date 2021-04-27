fin = open('words.txt')

for line in fin:
    word = line.strip()

    if 'e' in word:
        pass
    else:
        print(word)