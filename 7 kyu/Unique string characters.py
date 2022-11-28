# https://www.codewars.com/kata/5a262cfb8f27f217f700000b/python

def solve(a,b):
    res=[]
    for x in a:
        if x not in b:
            res.append(x)
    for i in b:
        if i not in a:
            res.append(i)
    return ''.join(res)
