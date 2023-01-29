from gmpy2 import is_prime


def backwards_prime(start, stop):
    re = []
    for i in range(start, stop + 1):
        if is_prime(i) and is_prime(int(str(i)[::-1])):
            if int(str(i)[::-1]) != int(str(i)):
                re.append(i)
    return re
