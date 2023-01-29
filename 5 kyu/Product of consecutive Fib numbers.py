from functools import reduce
def productFib(prod):
    fib = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]
    for  i in range(0,300):
        s= fib(i)*fib(i+1)
        if s == prod:
            return [fib(i),fib(i+1), True]
        if s>prod:
            return [fib(i),fib(i+1),False ]
