def check_three_and_two(array):
    a = array.count('a')
    b = array.count('b')
    c = array.count('c')
    if a == 3 and b == 2:
        return True
    if c == 3 and a == 2:
        return True
    if a == 3 and c == 2:
        return True
    if c == 3 and b == 2:
        return True
    if b == 3 and c == 2:
        return True
    if b == 3 and a == 2:
        return True
    return False
