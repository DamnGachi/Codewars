def solve(a, b):
    bob = 0
    alice = 0
    for i in range(0, len(a)):
        if a[i] > b[i]:
            alice += 1
        if b[i] > a[i]:
            bob += 1
    if alice > bob:
        return f'{alice}, {bob}: Alice made "Kurt" proud!'
    if alice < bob:
        return f'{alice}, {bob}: Bob made "Jeff" proud!'
    if alice == bob:
        return f'{alice}, {bob}: that looks like a "draw"! Rock on!'
