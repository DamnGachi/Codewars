import re
def insert_dash(num):
    regex = r"(?<=[13579])(?=[13579])"
    return re.sub(regex,'\1-\2', str(num)).replace('\x01','').replace('\x02','').replace('\x03','')

"""
import re
def insert_dash(num):
    return re.sub(r'([13579])(?=[13579])', r'\1-', str(num))
"""
