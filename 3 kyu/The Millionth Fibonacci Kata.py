from fibonacci import fibo

n = -96


def fib(n):
    if n == 1:
        return n
    if n % 2 != 0:
        last = 1
        last2 = 0
        result = 0
        for i in range(2, abs(n) + 1):
            result = last + last2
            last2 = last
            last = result
        return result
    if n < 0 and n % 2 == 0:
        last = 1
        last2 = 0
        result = 0
        for i in range(2, abs(n) + 1):
            result = last + last2
            last2 = last
            last = result
        return (result * -2) + result
    last = 1
    last2 = 0
    result = 0
    for i in range(2, abs(n) + 1):
        result = last + last2
        last2 = last
        last = result
    return result


print(fib(n))
