from gmpy2 import next_prime, digits

"""MY BEST SOLUTION"""
n = [25023]


def minimum_number(n):
    g = sum(n)
    if g <= 0 or g == 1:
        return False
    i = 2
    while (i <= g ** 0.5):
        if g % i == 0:
            return g
        i += 1
    return g


def minimum_number1(n):
    s = sum(n)
    s1 = s + (next_prime(s - 1) - s)
    return int(s1.digits()) - minimum_number(n)


print(minimum_number1(n))

"""KATA SOLUTION"""


def minimum_number1(n):
    g = sum(n)
    if g <= 0 or g == 1:
        return False
    i = 2
    while (i <= g ** 0.5):
        if g % i == 0:
            return g
        i += 1
    return g


def minimum_number2(n):
    s = sum(n)
    s1 = s + (next_prime(s - 1) - s)
    return int(s1.digits())


def minimum_number(n):
    return minimum_number2(n) - minimum_number1(n)
