
from gmpy2 import is_prime
import timeit

a, b = 1, 10000000


def solve(a, b):
    res = []
    count = 0
    for i in range(a, b):
        x = int(str(i)[-2:])
        s = int(str(i)[0:2])
        if is_prime(s):
            i *= i
        g = int(str(i)[0:2])
        y = int(str(i)[-2:])
        if is_prime(g):
            if x == y:
                count += 1
    return count


print(solve(a, b))
