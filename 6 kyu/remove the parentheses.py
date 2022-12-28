import re
def remove_parentheses(s):
    n = 1
    while n:
        s, n = re.subn(r'\([^()]*\)', '', s)
    return s 