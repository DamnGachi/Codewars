import re


def kebabize(string):
    text = re.sub(r'[0-9]', '', string)
    return re.sub(r'(?<!^)(?=[A-Z])', '-', text).lower()
