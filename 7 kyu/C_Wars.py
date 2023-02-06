def initials(name):
    res=[]
    name=name.split()
    for x in name[:-1]:
        res.append(x[0].title())
    res.append(name[-1])
    return '.'.join(res).title()
