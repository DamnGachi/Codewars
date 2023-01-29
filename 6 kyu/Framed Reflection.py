def mirror(text):
    text = text.split()
    max_ = len(sorted(text, key=len, reverse=True)[0])
    r = [x[::-1] + ' ' * (max_ - (len(x))) for x in text]
    s = '*' * (max_ + 4)
    return s + '\n* ' + ' *\n* '.join(r) + ' *\n' + s
