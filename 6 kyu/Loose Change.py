def loose_change(cents):
    pennies = 1
    nickels = 5
    dimes = 10
    quarters = 25

    change_dict = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    if cents < 1:
        return change_dict
    quert = cents // quarters
    if quert >= 1:
        change_dict['Quarters'] = quert
    s1 = cents - (quarters * quert)
    dime = s1 // dimes
    if dime >= 1:
        change_dict['Dimes'] = dime
    s2 = s1 - (dime * dimes)
    nick = s2 // nickels
    if nick >= 1:
        change_dict['Nickels'] = nick
    s3 = s2 - (nick * nickels)
    pennie = s3 // pennies
    if pennie >= 1:
        change_dict['Pennies'] = pennie
    return change_dict
