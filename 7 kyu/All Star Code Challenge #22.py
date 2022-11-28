# https://www.codewars.com/kata/5865cff66b5699883f0001aa/python
def to_time(seconds):
    minutes = seconds // 60
    hour=seconds// 3600
    minutes = minutes-(hour*60)
    return f'{hour} hour(s) and {minutes} minute(s)'