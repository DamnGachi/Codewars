def hydrate(d):
    res=[]
    for i in d:
        if i.isdigit():
            res.append(int(i))
    s=sum(res)
    if s==1:
        return str(s)+' glass of water'
    return str(s)+' glasses of water'
