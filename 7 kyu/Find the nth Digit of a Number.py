# https://www.codewars.com/kata/577b9960df78c19bca00007e/python

def find_digit(num, nth):
    try:
        if nth - 1 < 0:
            return -1
        s = str(num)[::-1]
        return int(s[nth - 1])
    except IndexError:
        return 0
