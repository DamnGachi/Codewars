def bingo(array):
    count = 0
    res = []
    s = "BINGO"
    for i in s:
        res.append(ord(i) - 64)
    for x in set(array):
        if x in res:
            count += 1
    return 'WIN' if count >= 5 else 'LOSE'
