import ipaddress


def ipv4_address(address):
    try:
        return True if ipaddress.IPv4Address(address) else False
    except Exception as error:
        return False
