# https://www.codewars.com/kata/598f76a44f613e0e0b000026/python


import re


def sum_of_integers_in_string(s):
    s = [int(x) for x in re.findall(r'-?\d+\d*', s)]
    return sum(s)
