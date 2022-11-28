

ip = "128.32.10.1"


def ip_to_int32(ip):
    standard_len = 10
    res = []
    res1 = []
    ip = ip.split('.')
    for i in ip:
        res.append(bin(int(i)))
    for x in res:
        s = standard_len - len(x)
        s = x.replace('0b', '0' * s)
        res1.append(s)
    return int(''.join(res1), 2)


print(ip_to_int32(ip))
from ipaddress import IPv4Address

def ip_to_int32(ip):
  return int(IPv4Address(ip))