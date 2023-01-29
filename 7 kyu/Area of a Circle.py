import math
def circle_area(r):

    try:
        if r<0:
            return False
        return round(math.pi*(r**2),2)
    except:
        return False
