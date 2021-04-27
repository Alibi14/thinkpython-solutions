

def backward_func(word):
    index = 0
    while abs(index) < len(word):
        letter = word[index-1]
        print(letter)
        print(index, "\n")
        index += -1


backward_func("alibi")