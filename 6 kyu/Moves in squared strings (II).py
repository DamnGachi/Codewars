def rot(strng):
    return strng[::-1]


def selfie_and_rot(strng):
    s = len(strng.split()[0])
    s1 = '.' * s
    return f'{s1}\n'.join(strng.split()) + f'{s1}\n{s1}' + f'\n{s1}'.join(strng[::-1].split())


def oper(fct, s):
    return fct(s)


if __name__ == '__main__':
    print(selfie_and_rot(
        strng='xZBV\njsbS\nJcpN\nfVnP'))
