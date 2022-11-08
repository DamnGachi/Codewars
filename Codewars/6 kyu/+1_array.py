arr = [2, 3, 9]


def up_array(arr):
    s = arr.pop()
    s = s + 1
    res = []
    for i in arr:
        res.append(int(str(i)))
    res.append(int(str(s)))
    return res


print(up_array(arr))
