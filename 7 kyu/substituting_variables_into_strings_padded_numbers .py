# https://www.codewars.com/kata/51c89385ee245d7ddf000001/python

def solution(value):
    s = len(str(value))
    array = '00000'
    return 'Value is ' + array[s:] + str(value)
