def string_merge(s1, s2, letter):
    sind1=s1.index(letter)
    sind2=s2.index(letter)
    return s1[:sind1] + s2[sind2:] 
