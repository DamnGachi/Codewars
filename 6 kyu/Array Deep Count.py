def deep_count(a):
    result = 0
    for i in range(len(a)):
        if type(a[i]) is list:
            result += deep_count(a[i])
        result += 1
    return result


print(deep_count(a=["x", "y", ["z"]]))