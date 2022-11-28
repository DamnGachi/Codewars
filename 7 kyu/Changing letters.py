def swap(st):
    vowels = ['a', 'e', 'i', 'o', 'u']
    second = ''
    for letter in st:
        if letter in vowels:
            second = second + letter.upper()
        else:
            second = second + letter
    return second
