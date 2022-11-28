def remove_rotten(bag):
    if bag == None:
        return []
    return ' '.join(bag).replace('rotten', '').lower().split()
