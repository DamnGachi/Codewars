def find_smallest(numbers, to_return):
    m = min(numbers)
    if to_return == 'index':
        return numbers.index(m)
    return m
