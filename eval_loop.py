import math


def eval_loop():
    while True:
        a = str(input())
        if a == "done":
            print(a)
            break
        b = eval(a)

        print(b)




eval_loop()


