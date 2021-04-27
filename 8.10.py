def is_polindrome(word):
    if word[0::1] == word[::-1]:
        return True
    else:
        return False


print(is_polindrome('aziza'))
