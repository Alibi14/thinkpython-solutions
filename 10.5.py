def chop(x):
    del x[:1]
    del x[-1:]
    print(x)


chop([1, 2, 3, 4])
