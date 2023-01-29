def geometric_sequence_elements(a, r, n):
    res=[a]
    for i in range(1,n):
        res.append(res[-1]*r)
    return ', '.join([str(x) for x in res])
