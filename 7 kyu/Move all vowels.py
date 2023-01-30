def move_vowels(s):
    vowels='aeiou'
    sogl= [x for x in s if x not in vowels ]
    gl=[x for x in s if x in vowels]
    return ''.join(sogl)+''.join(gl)