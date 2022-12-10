def make_backronym(acronym):
    res=[]
    for i in acronym:
        res.append(dictionary.get(i.upper()))
    return ' '.join(res)