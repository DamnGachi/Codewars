from collections import Counter
def sum_no_duplicates(l):
    res=[]
    c = Counter(l)
    for x in c.items():
        if x[1]==1:
            res.append(x[0])
    return sum(res)
