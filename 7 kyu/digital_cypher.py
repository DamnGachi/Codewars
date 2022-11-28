message, key = 'scout', 19391


def encode(message, key):
    x = 0
    res = []
    for i in message:
        s = (ord(i) - 96) + int(str(key)[x])
        x += 1
        res.append(s)
        if x >= len(str(key)):
            x = 0
    return res


print(encode(message, key))
