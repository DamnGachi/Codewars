# https://www.codewars.com/kata/5742e725f81ca04d64000c11/train/python

from gmpy2 import is_prime


def prime_or_composite(n):
    if is_prime(n):
        return "Probable Prime"
    return "Composite"
