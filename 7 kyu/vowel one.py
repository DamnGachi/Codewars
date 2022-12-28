def vowel_one(s):
    vowels = 'aeiouAEIOU'
    s=s.replace('123','000')
    for vowel in vowels:
        s = s.replace(vowel, '1')
    for i in s:
        if i!='1':
            s = s.replace(i, '0')
    return s
