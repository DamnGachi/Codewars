import re

def autocomplete(ih, d):
    o=re.sub(r'[$|@|&|%|#|*| |^|_|)|(|!|~|+|0-9]','',ih)
    s=len(o)
    res=[]
    for i in d:
        if i.lower()[0:s]==o:
            res.append(i)
    return res[:5]
