# def count_ones(left, right):
#     res = []
#     for i in range(left, right + 1):
#         res.append(bin(i)[2::])
#     return ''.join(res).count('1')

l, r = 77996950831736, 129221127259865

res = []
for i in range(l, r + 1):
    res.append(bin(i)[2::])
print( ''.join(res).count('1'))
