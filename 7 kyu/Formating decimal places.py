def two_decimal_places(number):
    s=str(number).split('.')[0]
    return float(s+'.'+str(number).split('.')[1][:2])
