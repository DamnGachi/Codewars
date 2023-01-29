def solve(arr):
    res = []
    for v in arr[::-1]:
        if not res or res[-1] < v: res.append(v)
    return res[::-1]
