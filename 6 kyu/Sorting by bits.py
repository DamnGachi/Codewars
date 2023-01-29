def sort_by_bit(arr):
    arr.sort(key=lambda x:(bin(x).count('1'), x))   # they wanted to modify the input

    return arr