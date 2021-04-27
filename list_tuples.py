from typing import Any, Tuple, Iterator

s = 'abc'

t = ['b', 'a', 'c']

new: Iterator[tuple[Any, int]] = zip(s, t)


for one in new:
    print(one)


new_list = list(zip(s,t))

# for letter, number in new_list:
    # print(letter, number)


def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False


print(has_match('abc', 'bac'))