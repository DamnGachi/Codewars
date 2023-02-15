from collections import Counter


def odd_ones_out(numbers):
    re = []
    s = Counter(numbers)
    for key in s.items():
        if key[1] % 2 != 0:
            re.append(key[0])
    return [x for x in numbers if x not in re]
