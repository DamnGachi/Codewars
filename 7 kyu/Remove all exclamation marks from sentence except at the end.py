
def remove(a):
    res=[]
    s=a[::-1].split()
    for i in s[0]:
        if i=='!':
            res.append(i)
        else:
            break
    return a.replace('!','')+''.join(res)
