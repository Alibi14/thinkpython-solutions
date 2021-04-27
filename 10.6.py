def is_anagram(var1, var2):
    var1 = list(var1)
    var2 = list(var2)

    for i in range(len(var1)):
        if len(var1) != len(var2) or var1[i] not in var2:
            return False


    return True



print(is_anagram('listen', 'silent'))

