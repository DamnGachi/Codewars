def even_or_odd(s):
    s1 = ([int(i) for i in s if int(i) % 2 == 0])
    s2 = ([int(i) for i in s if int(i) % 2 != 0])
    if sum(s1) == sum(s2):
        return 'Even and Odd are the same'
    if sum(s1) > sum(s2):
        return 'Even is greater than Odd'
    return 'Odd is greater than Even'
