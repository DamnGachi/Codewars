# https://www.codewars.com/kata/570e8ec4127ad143660001fd/python

def billboard(name, price=30):
    name=len(name)
    count=0
    for i in range(name):
        count+=price
    return count