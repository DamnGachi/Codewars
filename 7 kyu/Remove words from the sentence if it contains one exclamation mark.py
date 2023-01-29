def remove(s):
    res=[]
    for i in s.split():
        if not i.count('!')==1:
            res.append(i)
    return ' '.join(res)
