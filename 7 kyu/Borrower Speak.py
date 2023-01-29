import re
def borrow(s):
    regex = re.compile('[@.,;_ !#$%^&*()<>?/\|}{~:]')
    return re.sub(regex,'',s).lower()
