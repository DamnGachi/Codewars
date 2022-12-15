def time_correct(t):
    try:
        if ":" not in t:
            return None
        if t[1].isalpha():
            return None
    except:
        return None
    s = t.split(':')
    s1 = int(s[0])
    s2 = int(s[1])
    s3 = int(s[2])
    if int(s[2]) >= 60:
        s2 += 1
        s3 -= 60
    if int(s[1]) >= 60:
        s1 += 1
        s2 -= 60
    if int(s[0]) >= 24:
        s4 = (s1 // 24)
        s1 = s1 - (24 * s4)
    if len(str(s1)) <= 1:
        s1 = '0' + str(s1)
    if len(str(s2)) <= 1:
        s2 = '0' + str(s2)
    if len(str(s3)) <= 1:
        s3 = '0' + str(s3)
    return str(s1) + ':' + str(s2) + ':' + str(s3)
