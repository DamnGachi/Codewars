def solve(a, b):
    try:
        if a == 0 or b == 0:
            return [a, b]
        if a >= (2 * b):
            a = a - 2 * b
        if b >= 2 * a:
            b = b - 2 * a
        return solve(a, b)
    except RuntimeError:
        return [a, b]
