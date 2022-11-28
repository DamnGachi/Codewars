x, n = 3, 3


def squares(x, n):
    res = []
    for i in range(x, n*n):
        res.append(i)
    return res


print(squares(x, n))
