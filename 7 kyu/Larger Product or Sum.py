import math


def sum_or_product(array, n):
    m = sum(sorted(array, reverse=True)[0:n])
    l = math.prod(sorted(array)[0:n])
    if m > l:
        return 'sum'
    if m == l:
        return 'same'
    return 'product'
