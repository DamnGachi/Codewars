def single_digit(n):
    if n < 9:
        return n
    else:
        s = sum(list(map(int, bin(n)[2:])))
        return single_digit(s)
