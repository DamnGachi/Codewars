def move_ten(st):
    res = []
    for i in st:
        s = ord(i) + 10
        if s > 122:
            res.append(chr((((ord(i) - 96) + 10) - 26) + 96))
        elif s <= 122:
            res.append(chr(s))
    return ''.join(res)
