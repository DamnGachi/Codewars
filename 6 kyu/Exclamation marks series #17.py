def balance(left, right):
    l1 = (left.count('!') * 2) + (left.count('?') * 3)
    r1 = (right.count('!') * 2) + (right.count('?') * 3)
    if l1 > r1:
        return "Left"
    if l1 == r1:
        return "Balance"
    return 'Right'
