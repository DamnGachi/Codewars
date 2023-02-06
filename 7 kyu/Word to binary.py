def word_to_bin(word):
    return ['0'+(bin(ord(x))[2:]) for x in word]
