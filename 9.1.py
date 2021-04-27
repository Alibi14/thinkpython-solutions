fin = open('words.txt')

for line in fin:
    word = line.strip()
    if len(line) > 20:
        print(word)