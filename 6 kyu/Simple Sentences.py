def make_sentences(parts):
    parts.append('.')
    s = ' '.join(parts).replace(' .', '.').replace(' ,', ',')
    cot = s.count('.')
    return s.replace('.' * cot, '.')
