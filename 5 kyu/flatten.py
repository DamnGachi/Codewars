from itertools import chain


def flatten(*args):
    s = sum(([i] if not isinstance(i, list) else i for i in args), [])
    x = sum(([i] if not isinstance(i, list) else i for i in s), [])
    y = sum(([i] if not isinstance(i, list) else i for i in x), [])
    j = sum(([i] if not isinstance(i, list) else i for i in y), [])
    u = sum(([i] if not isinstance(i, list) else i for i in j), [])
    h = sum(([i] if not isinstance(i, list) else i for i in u), [])
    k = sum(([i] if not isinstance(i, list) else i for i in h), [])
    return k
