def show_sequence(n):
    res = []
    rea = []
    for i in range(n + 1):
        rea.append(i)
        res.append(str(i))
    if n > 0:
        return '+'.join(res) + ' = ' + str(sum(rea))
    elif n == 0:
        return '+'.join(res) + '=' + '0'
    return str(n) + '<'  '0'
