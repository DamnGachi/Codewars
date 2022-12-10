def find_admin(lst, lang):
    res = []
    for i in lst:
        if lang in i.values() and 'yes' in i.values():
            res.append(i)
    return res
