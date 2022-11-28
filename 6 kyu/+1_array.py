arr = [0]

global s


def up_array(arr):
    res = []
    if len(arr)==1:
        if arr[0]==0:
            return 0
    try:
        for i in arr:
            if i > 9:
                return None
            res.append(str(i))
            s = ''.join(res)
            m = int(s) + 1
        if arr[0] == 0:
            t = '0' + str(m)
            return [int(a) for a in t]
        return [int(a) for a in str(m)]
    except:
        return None


print(up_array(arr))
