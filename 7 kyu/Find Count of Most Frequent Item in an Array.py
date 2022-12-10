def most_frequent_item_count(collection):
    res = []
    try:
        for i in range(-11, 11):
            res.append(collection.count(i))
        return max(res)
    except IndexError:
        return 0
