import numpy as np

a = [[1, 2, 3],
     [3, 2, 1],
     [1, 1, 1]],
b = [[2, 2, 1],
     [3, 2, 3],
     [1, 1, 3]]


def matrix_addition(a, b):
    w = np.array(a)
    s = np.array(b)
    c = w + s
    print(s)
    return c.tolist()



print(matrix_addition(a, b))
