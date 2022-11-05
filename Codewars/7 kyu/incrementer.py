nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8]


def incrementer(nums):
    res = []
    rs = []
    for i in range(1, len(nums) + 1):
        res.append(i)
    s = list(map(sum, zip(res, nums)))
    for x in s:
        rs.append(int(str(x)[-1]))
    return rs
