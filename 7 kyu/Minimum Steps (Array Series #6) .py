# https://www.codewars.com/kata/5a91a7c5fd8c061367000002/python

def minimum_steps(numbers, value):
    num=sorted(numbers)
    count=0
    total=0
    for i in num:
        total+=i
        count+=1
        if total>=value:
            return count-1