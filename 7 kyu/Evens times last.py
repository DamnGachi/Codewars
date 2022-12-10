def even_last(numbers):
    res=[]
    try:
        for i,y in enumerate(numbers):
            if i%2==0:
                res.append(numbers[i])
        return sum(res)*numbers[-1]
    except IndexError:
        return 0
