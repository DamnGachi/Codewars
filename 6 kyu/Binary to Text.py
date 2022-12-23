import binascii


def binary_to_string(binary):
    try:
        n = int(binary, 2)
        return binascii.unhexlify('%x' % n).decode()
    except:
        return binary
