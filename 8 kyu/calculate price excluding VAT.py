# https://www.codewars.com/kata/5890d8bc9f0f422cf200006b/python
def excluding_vat_price(price):
    if price == None:
        return -1
    s = round(price / 115 * 15, 2)
    return round(price - s, 2)
