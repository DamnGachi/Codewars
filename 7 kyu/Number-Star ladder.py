def pattern(n):
    res=['1']
    for i in range(1,n):
        res.append(str(1)+('*')*(i)+str(i+1))
    return '\n'.join(res)