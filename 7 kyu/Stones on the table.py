def solution(stones):
    res=[]
    for i,y in enumerate(stones):
        if stones[i]==stones[i-1]:
            res.append(i)
    try:
        if res[0]==0:
            return len(res[1:])
        return len(res)
    except:
        return len(res)


def solution(stones):
    count=0
    for i in range(1,len(stones)):
        if stones[i-1]==stones[i]:
            count+=1
    return count
