def one(sq, fun):
    res=[]
    for i in sq:
        if fun(i):
            res.append(i)
    return True if len(res)==1 else False