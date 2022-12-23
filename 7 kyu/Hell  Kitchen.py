def gordon(a):
    bot = ['E', 'U', 'I', 'O']
    s = a.upper().replace('A', '@')
    for i in s:
        if i in bot:
            s = s.replace(i, '*')
    return '!!!! '.join(s.split()) + '!!!!'
