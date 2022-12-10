def longest_word(string_of_words):
    s = string_of_words.split()
    return sorted(s, key=len)[-1]
