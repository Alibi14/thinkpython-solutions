import random


def has_duplicates(var):
    var = list(var)
    var.sort()

    for i in range(len(var)-1):
        if var[i] == var[i+1]:
            return True

    return False


def people_in(var):
    t = []
    for i in range(var):
        var2 = random.randint(1, 365)
        t.append(var2)
    print(t)
    return t


def birthday_paradox(num_students, num_simulations):
    count = 0

    for i in range(num_simulations):
        t = people_in(num_students)
        if has_duplicates(t):
            count += 1

    print(count)
    return count


birthday_paradox(200, 10)
