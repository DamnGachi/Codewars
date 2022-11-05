def good_vs_evil(good, evil):
    res1 = []
    res2 = []
    for i in good.split():
        if i.isdigit():
            res1.append(int(i))
    for x in evil.split():
        if x.isdigit():
            res2.append(int(x))
    return good, evil
