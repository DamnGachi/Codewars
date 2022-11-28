# https://www.codewars.com/kata/56dbe0e313c2f63be4000b25/python

string = "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"


def vert_mirror(string):
    res = []
    s = string.split('\n')
    for i in s:
        res.append(i[::-1])
    return '\n'.join(res)


def hor_mirror(string):
    res = []
    s = string.split('\n')[::-1]
    for i in s:
        res.append(i)
    return '\n'.join(res)


def oper(fct, s):
    return fct(s)


print(vert_mirror(string))
