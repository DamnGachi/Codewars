# https://www.codewars.com/kata/552564a82142d701f5001228/python


def discover_original_price(price, sale):
    return round(price / (100 - sale) * 100, 2)
