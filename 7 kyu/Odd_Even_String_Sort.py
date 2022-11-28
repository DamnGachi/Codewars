# https://www.codewars.com/kata/580755730b5a77650500010c/python


def sort_my_string(s):
    res1 = []
    res2 = []
    index = -1
    for value in s:
        index += 1
        if index % 2 == 0:
            res1.append(value)
        if index % 2 != 0:
            res2.append(value)
    return ''.join(res1) + ' ' + ''.join(res2)
