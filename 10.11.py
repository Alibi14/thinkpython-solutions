def in_bisect(word_list,word):
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2

    if word_list[i] == word:
        return True

    if word_list[i] > word:
        return in_bisect(word_list[:i], word)
    else:
        return in_bisect(word_list[i+1:], word)


def reverse_pair(word_list, word):
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)
