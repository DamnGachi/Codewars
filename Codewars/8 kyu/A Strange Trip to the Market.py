
# https://www.codewars.com/kata/55ccdf1512938ce3ac000056/python

def is_lock_ness_monster(string):
    s1 = string.find('tree fiddy')
    s2 = string.find('three fifty')
    s3 = string.find('3.50')
    s4 = s1 + s2 + s3
    if s4 > 0:
        return True
    return False
