from gmpy2 import primorial, next_prime

n = 3


def num_primorial(n):
    res = []
    for i in range(1, n + 1):
        u = next_prime(i)
        res.append(u)
    return (res)


print(num_primorial(n))
