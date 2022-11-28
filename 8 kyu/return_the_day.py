# https://www.codewars.com/kata/59dd3ccdded72fc78b000b25/python
weekday = {
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday'}
error = 'Wrong, please enter a number between 1 and 7'


def whatday(number):
    return weekday.get(number, error)

