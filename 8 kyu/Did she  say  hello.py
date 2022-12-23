import re


def validate_hello(greetings):
    okay = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    o = re.sub(r'[$|@|&|%|#|*|,|?|^|:|;|.|_|)|(|!|~|+|0-9]', '', greetings)
    for i in o.split():
        if i.lower() in okay:
            return True
    return False
