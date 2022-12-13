def well(arr):
    res = []
    for i in arr:
        for x in i:
            try:
                res.append(x.lower())
            except:
                res.append(x)
    s = res.count('good')
    if s == 1 or s == 2:
        return 'Publish!'
    if s > 2:
        return 'I smell a series!'
    return 'Fail!'
