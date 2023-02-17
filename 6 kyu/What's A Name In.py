def name_in_str(strs, name):
    strs=strs.lower()
    name=name.lower()
    count=0
    res=[]
    try:
        for i,y in enumerate(strs):
            if strs[i]==name[count]:
                count+=1
                res.append(y)
        return ''.join(res) == name
    except:
        return True