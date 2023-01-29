from re import sub
def to_camel_case(text):
    try:
        text1 = sub(r"(_|-)+", " ", text).title().replace(" ", "")
        if text[0].isupper():
            return text1
        return text1[0].lower() + text1[1:]
    except IndexError:
        return ""
