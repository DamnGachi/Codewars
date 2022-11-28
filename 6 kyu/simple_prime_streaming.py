a, b = 20000, 5


def prime_generator(x):
    x = 50000
    prs = {}
    p = 1
    while p < x:
        if p not in prs:
            yield p
            prs[p * p] = [p]
        else:
            for s in prs[p]:
                prs.setdefault(s + p, []).append(s)
            del prs[p]
        p += 1
    return prs


def solve(a, b):
    x = 50000
    s = list(map(str, prime_generator(x)))[1::]
    s1 = ''.join(s)
    return s1[a:a + b]


print(solve(a, b))
