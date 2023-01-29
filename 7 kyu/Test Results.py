def test(r):
    counth = 0
    counta = 0
    countl = 0
    s = round(sum(r)/len(r), 3)
    for i in r:
        if i >= 9:
            counth += 1
        if 7 <= i <= 8:
            counta += 1
        if i <= 6:
            countl += 1
    if counta == 0 and countl == 0:
        return [s, {'h': counth,'a': counta,'l': countl}, 'They did well']
    return [s, {'h': counth,'a': counta,'l': countl}]
