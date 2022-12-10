def valid_spacing(s):
    s1 = len(s.split())
    if s == '':
        return True
    return True if s.count(' ') <= s1 - 1 else False
