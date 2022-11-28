ticket = [['KWMFTS', 70], ['MVRBFLDC', 89], ['SX', 72], ['OEWCEWF', 62], ['XNSAKB', 68]]
win = 2


def bingo(ticket, win):
    tickets = 0
    res = []
    for i in ticket:
        for x in i[0]:
            res.append(ord(x))
        if i[1] in res:
            tickets += 1
    if tickets < win:
        return 'Loser!'
    return 'Winner!'


print(bingo(ticket, win))
