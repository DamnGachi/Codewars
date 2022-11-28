s = 'vbMjOZOFSLgoxSi1dfwy4Xn rdEd9'


def changer(s):
    """
    def changer(s):
    return s.lower().translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'bcdEfghIjklmnOpqrstUvwxyzA'))
    """
    res = []
    res1 = []
    vowels = ['a', 'u', 'o', 'i', 'e']
    for i in s:
        if i.isalpha():
            res.append(ord(i) + 1)
        elif i.isdigit() or i.isspace():
            res.append(ord(i))
    s1 = ''.join(chr(x) for x in res)
    for p in s1.lower():
        if p in vowels:
            res1.append(p.title())
        if p not in vowels:
            res1.append(p.lower())
    return ''.join(res1).replace('[', 'A').replace('{','a')


print(changer(s))
