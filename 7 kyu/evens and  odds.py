# https://www.codewars.com/kata/583ade15666df5a64e000058/python
def evens_and_odds(n):
    if n % 2 == 0:
        return bin(n)[2:]
    return hex(n)[2:]
