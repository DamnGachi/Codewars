# https://www.codewars.com/kata/5878520d52628a092f0002d0/train/python

def string_transformer(s):
    s = s.swapcase()
    return ' '.join(s.split(' ')[::-1])
