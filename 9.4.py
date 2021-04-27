fin = open('words.txt')


def uses_only(word, letter):
    for char in word:
        if char not in letter:
            return False

    return True


letter = input("Letters need for words?\n")
count = 0

for line in fin:
    word = line.strip()
    if uses_only(word, letter):
        count += 1
        print(word)

percentage = (count / 113809) * 100
print(percentage)


