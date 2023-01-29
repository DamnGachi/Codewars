def solution(n,d):
    if d<=0:
        return []
    return [int(x) for x in str(n)[-d:]]
