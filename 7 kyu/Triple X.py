def triple_x(s):
    try:
        s1 = s.index('x')
        if s[s1 + 1] == 'x' and s[s1 + 2] == 'x':
            return True
        return False
    except ValueError:
        return False
    except IndexError:
        return False
