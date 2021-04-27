def has_duplicates(var):
    var = list(var)
    var.sort()
    for i in range(len(var) - 1):
        if var[i] == var[i + 1]:
            return True

    return False


print(has_duplicates('solo'))
