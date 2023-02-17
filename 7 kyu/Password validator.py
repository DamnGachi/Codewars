import re


def password(string):
    pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$"
    if re.fullmatch(pattern, string):
        return True
    return False
