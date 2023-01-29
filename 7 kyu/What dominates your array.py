from collections import Counter

arr = [10, 2, 10, 8, 8, 10, 8]


def dominator(arr):
    s = Counter(arr)
    try:

        print(s)
        return (sorted(s.items(), key=lambda x: x[1], reverse=True))[0][0]
    except:
        return -1


print(dominator(arr))
