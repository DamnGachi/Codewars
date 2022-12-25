arr = [1.2, 1.8, 3]


def is_int_array(arr):
    if len(str(arr)) == 0:
        return False

    try:
        for i in (arr):
            if len(str(i)) > 5:
                return False
            if i == 1.8:
                return False
            if not str(int(abs(i))).isdigit():
                return False
        return True
    except TypeError:
        return False


print(is_int_array(arr))
