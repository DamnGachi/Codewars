import numpy as np

s = [-7, -42, -809, -14, -12]


def max_gap(s):
    s = sorted(s)
    index = np.argmax(np.diff(s))
    result = s[index] - s[index + 1]
    return abs(result)


print(max_gap(sorted(s)))
