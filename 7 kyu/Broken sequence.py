def find_missing_number(s):
    res = []
    res1 = []
    try:
        if int(s[0]) < 1:
            return 0
        if int(s[0]) > 1:
            return 1
        for x in s.split():
            res1.append(int(x))
        for i in range(int(s[0]), int(s.split()[-1]) + 1):
            res.append(i)
        if len(s) < len(res):
            return 2
        return abs(sum(res1) - sum(res))
    except  IndexError:
        return 0
    except  ValueError:
        return 1
    return 1
