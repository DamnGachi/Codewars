import collections, re


def ordered_count(inp):
    res = []
    for (k, v) in collections.Counter(re.compile('[^a-zA-Z]').sub(' ', inp)).items():
        res.append(k)
        res.append(v)
    return res
