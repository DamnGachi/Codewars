import math

MAX = 1000000
primes = []
n = 22


def sieveSundaram():
    marked = [False] * (int(MAX / 2) + 1)

    for i in range(1, int((math.sqrt(MAX) - 1) / 2) + 1):
        for j in range(((i * (i + 1)) << 1), (int(MAX / 2) + 1), (2 * i + 1)):
            marked[j] = True

    primes.append(2)

    for i in range(1, int(MAX / 2)):
        if (marked[i] == False):
            primes.append(2 * i + 1)
    return primes


sieveSundaram()


def num_primorial(n):
    result = 1
    for i in range(n):
        result = result * primes[i]
    return result
