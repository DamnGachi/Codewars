from collections import Counter


def first_non_repeated(s):
    z = Counter(s)
    sorted_keys = sorted(z, key=z.get)
    if min(z.values()) == 1:
        return sorted_keys[0]
    return None
