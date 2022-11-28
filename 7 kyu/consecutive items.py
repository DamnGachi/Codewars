def consecutive(arr, a, b):
    mas = [-1, 0, 1]
    a1 = arr.index(a)
    b1 = arr.index(b)
    s1 = a1 - b1
    if s1 in mas:
        return True
    return False
