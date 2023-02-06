def get_larger_numbers(a, b):
    res=[]
    for i in range(0,len(a)):
        if a[i]>=b[i]:
            res.append(a[i])
        if a[i]<b[i]:
            res.append(b[i])
    return res
