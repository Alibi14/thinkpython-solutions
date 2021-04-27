fin = open('words.txt')


def uses_all(word, letters):
    for letter in letters:
        if letter not in word:
            return False

    return True


letters = input("What letters is necessary?\n Type here: ")
count = 0
supercount = 0

for line in fin:
    word = line.strip()
    supercount += 1
    if uses_all(word, letters):
        print(word)
        count += 1

print(count)
print(supercount)

percentage = (count / supercount) * 100

print(percentage, "% of all words has the required letters")
