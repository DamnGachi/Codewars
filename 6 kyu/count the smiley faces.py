arr=[':)',':(',':D',':O',':;']

def count_smileys(arr):
    s1=arr.count(':)')
    s2=arr.count(';-)')
    s3=arr.count(';~)')
    s4=arr.count(';)')
    s5=arr.count(':~)')
    s6=arr.count(':-)')
    s7=arr.count(':D')
    s8=arr.count(';D')
    s9=arr.count(':-D')
    s10=arr.count(';-D')
    s11=arr.count(':~D')
    s12=arr.count(';~D')
    return s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11+s12

"""
from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
"""
