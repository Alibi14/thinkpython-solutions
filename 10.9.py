fin = open('words.txt')

new_list = []


def adding_in(words):
    new_list.append(words)
    return new_list


for line in fin:
    word = line.strip()
    adding_in(word)


print(new_list)







