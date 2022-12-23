from decimal import Decimal

d = 0.42


def damn(d):
    d = Decimal(str(d))
    nominator, denominator = d.as_integer_ratio()
    # if nominator<denominator:
    #     return denominator/nominator
    return nominator,denominator


print(damn(d))