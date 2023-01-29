
def sortme(words):
    titles=[]
    res=[]
    for i in words:
        if i[0].isupper():
            titles.append(i)
    s=sorted((' '.join(words).lower()).split())
    for x in s:
        if x.capitalize() in titles:
            res.append(x.capitalize())
        if x.capitalize() not in titles:
            res.append(x)
    return res


print(sortme(words=["Hello", "there", "I'm", "fine"]))
