fin = open('words.txt')


def avoids(word, letters):
    for char in word:
        if char in letters:
            return False

    return True


letter = input('What letters to exclude?')
count = 0
for line in fin:
    word = line.strip()
    if avoids(word, letter):
        count += 1
        print(word)


percent = (count / 113809) * 100

print(str(percent) + "% of the words don't have" + letter)



