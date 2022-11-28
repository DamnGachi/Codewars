town = "~O~O~O~OP~O~OO~"


def count_deaf_rats(town):
    return town.replace(' ', '')[::2].count('O')


print(count_deaf_rats(town))
