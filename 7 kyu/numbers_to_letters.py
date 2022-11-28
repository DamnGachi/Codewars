# https://www.codewars.com/kata/57ebaa8f7b45ef590c00000c/python
def switcher(arr):
    alp = ' ?!abcdefghijklmnopqrstuvwxyz'[::-1]
    return ''.join(alp[int(i) - 1] for i in arr)
