def is_lucky(n):
    s=str(n)
    return True   if   sum([int(x) for x in s])%9==0  else False
