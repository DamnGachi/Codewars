pairs = {'x': 9, 2: -5, 'c': -9, 0: -6, 'a': -2}


def solution(pairs):
    return sorted(pairs)


print(solution(pairs))
assert pairs == "0 = -6,2 = -5,a = -2,c = -9,x = 9"
