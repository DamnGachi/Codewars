def is_nice(arr):
    return bool(arr) and all(n + 1 in arr or n - 1 in arr for n in arr)
