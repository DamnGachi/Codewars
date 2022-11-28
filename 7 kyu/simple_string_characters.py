import string

s = "P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"


def solve(s):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for i in s:
        if i.isupper():
            count1 += 1
        if i.islower():
            count2 += 1
        if i.isdigit():
            count3 += 1
        if i in string.punctuation:
            count4 += 1
    return [count1, count2, count3, count4]


print(solve(s))
