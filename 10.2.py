def cumulative_sum(newArray):
    res = []
    sum = 0
    for i in newArray:
        sum = sum + i
        res.append(sum)
    print(res)
    return res

cumulative_sum([1,2,3])
# [1,3,6]

