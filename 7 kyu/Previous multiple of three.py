def prev_mult_of_three(n):
    if n % 3 == 0:
        return n
    for i in range(-1, (len(str(-n)))):
        try:
            s = int(str(n)[:i])
            if s % 3 == 0:
                return s
            return prev_mult_of_three(s)
        except:
            return None
