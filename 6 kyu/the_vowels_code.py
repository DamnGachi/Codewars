# https://www.codewars.com/kata/53697be005f803751e0015aa/python

vowels = {"a": "1", "e": "2", "i": "3", "o": "4", "u": "5"}


def encode(st):
    for w in vowels:
        st = st.replace(w, vowels[w])
    return st


def decode(st):
    for k, v in vowels.items():
        st = st.replace(v, k)
    return st
