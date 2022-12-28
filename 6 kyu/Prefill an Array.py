def prefill(n,v=''):
    try:
        try:
            return [v]*int(n)
        except TypeError:
            return 'undefined'
    except ValueError:
        return f'{n} is invalid'    