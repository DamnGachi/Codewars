def multiples(s1, s2, s3):
    return [x for x in range(s1, s3) if x % s1 == 0 and x % s2 == 0]
